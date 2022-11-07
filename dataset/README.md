# Dataset

This dataset is used for NYU CV Final Project: build a AI-generated v.s. real-life-captured image classifier. We built it by generating images from real photos using Stable-Diffusion-based image-to-image model.

![](https://user-images.githubusercontent.com/23469706/200314769-ddd1690f-a261-4110-9a99-08fd908517c0.png)

## Stable Diffusion

The model we use is a pretrained conditioned Stable Diffusion model that accepts CLIP image embedding rather than text embeddings. So it's capable of generating variations from any given image embedding. The repository for the model is at https://github.com/LambdaLabsML/lambda-diffusers.

## Build Dataset

In order to train a classifier that can distinguish between real and generated images, we need a dataset of real and generated images. We started with real photos from existing public datasets. Then, we use Stable-Diffusion-based image-to-image model to generate images from real photos. This way, we ended up with a labeled dataset of real photos and generated photos.

### Download raw dataset and extract it

A shell script is provided to download and extract the raw dataset. The script will download the raw dataset to `raw` directory.

```bash
./download_indoor.sh
```

### Run `dataset_factory` to process raw dataset

Processing the raw dataset includes generating new images using Stable Diffusion model and cropping and resizing images to 256x256.

```bash
./dataset_factory
```

or

```bash
./dataset_factory -d raw -o processed -s 256
```

The processed dataset will be saved to `processed` folder.

## Dataset Structure

The processed dataset is organized as follows:

```
processed
├── ai
│   ├── living_room_1patio_view.jpg
│   ├── living_room_2living_room.jpg
│   └── ...
├── original
│   ├── living_room_1patio_view.jpg
│   ├── living_room_2living_room.jpg
│   └── ...
```
