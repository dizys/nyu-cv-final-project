import os
from pathlib import Path
from typing import List, Tuple, Union
from .lambda_diffusers import StableDiffusionImageEmbedPipeline
from PIL import Image
import torch
from fastprogress import progress_bar

class DatasetFactory:
    def __init__(self, original_image_folder: Union[str, Path], output_folder: Union[str, Path], output_image_size: int = 256):
        self.original_image_folder = Path(original_image_folder)
        self.output_folder = Path(output_folder)
        self.output_image_size = output_image_size
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"
            print("Warning: CUDA is not available. This is running on CPU and will be very slow.")
        pipe = StableDiffusionImageEmbedPipeline.from_pretrained("lambdalabs/sd-image-variations-diffusers")
        self.pipe = pipe.to(self.device)

    def _glob_all_original_images(self) -> List[Path]:
        return [path for path in self.original_image_folder.glob("**/*.{jpg,jpeg,png}")]

    def _init_folders(self):
        self.output_folder.mkdir(parents=True, exist_ok=True)
        (self.output_folder / "original").mkdir(parents=True, exist_ok=True)
        (self.output_folder / "ai").mkdir(parents=True, exist_ok=True)

    def get_image_paths(self) -> Tuple[List, List, List]:
        origin_image_paths = self._glob_all_original_images()
        output_original_image_paths = []
        output_ai_image_paths = []

        for image_path in origin_image_paths:
            relpath = os.path.relpath(image_path, self.original_image_folder)
            relpath = relpath.replace(os.path.sep, "_")
            dot_index = relpath.rfind(".")
            relpath = relpath[:dot_index]
            output_original_image_paths.append(self.output_folder / "original" / f"{relpath}.jpg")
            output_ai_image_paths.append(self.output_folder / "ai" / f"{relpath}.jpg")

        return origin_image_paths, output_original_image_paths, output_ai_image_paths

    def _center_crop_and_resize_image(self, image: Image.Image) -> Image.Image:
        width, height = image.size
        if width != height:
            if width > height:
                left = (width - height) / 2
                right = left + height
                top = 0
                bottom = height
            else:
                left = 0
                right = width
                top = (height - width) / 2
                bottom = top + width
            image = image.crop((left, top, right, bottom))
        image = image.resize((self.output_image_size, self.output_image_size))
        return image

    def generate_one_ai_image(self, original_image: Image.Image) -> Image.Image:
        num_samples = 1
        image = self.pipe(num_samples * [original_image], guidance_scale=3.0)
        image = image["sample"]
        return image[0]

    def generate(self):
        self._init_folders()

        print(f"Generating images from {self.original_image_folder} to {self.output_folder}...")

        origin_image_paths, output_original_image_paths, output_ai_image_paths = self.get_image_paths()
        dataset_size = len(origin_image_paths)
        assert dataset_size == len(output_original_image_paths) == len(output_ai_image_paths)
        print(f"- Found {dataset_size} images to process.")

        for index in progress_bar(range(dataset_size)):
            origin_image_path = origin_image_paths[index]
            output_original_image_path = output_original_image_paths[index]
            output_ai_image_path = output_ai_image_paths[index]

            if output_original_image_path.exists() and output_ai_image_path.exists():
                print(f"- Skip {origin_image_path} because it has already been processed.")
                continue

            origin_image = Image.open(origin_image_path)
            output_original_image = self._center_crop_and_resize_image(origin_image)
            output_ai_image = self._center_crop_and_resize_image(self.generate_one_ai_image(origin_image))

            output_original_image.save(output_original_image_path)
            output_ai_image.save(output_ai_image_path)

        print("- Done.")
