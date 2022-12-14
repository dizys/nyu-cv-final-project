# nyu-cv-final-project

NYU CV Final Project: build a AI-generated v.s. real-life-captured image classifier

## Getting Started

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

or when on HPC, to avoid exceeding home inode quota:

```bash
pip install -r requirements.txt --no-cache-dir

# or

pip install -r requirements.txt --no-index --find-links=/scratch/$USER/pip_cache
```

## Get Dataset

We custom built the dataset ourselves from existing public real-photo datasets. We used diffusion-model-based image-to-image models to generate images from real photos, including Stable Diffusion and DALLE2(available only as APIs). This way, we ended up with a labeled dataset of real photos and generated photos.

-   How we built it: [dataset/README.md](dataset/README.md)
-   Download datasets: [Dataset Releases](https://github.com/dizys/nyu-cv-final-project/releases/tag/dataset)

## Experiment Notebooks

Train on the main dataset:

-   [ResNet34 Train](notebooks/fastai_resnet34_train.ipynb)
-   [ResNet50 Train](notebooks/fastai_resnet50_train.ipynb)

Test on other datasets:

-   [ResNet34 Test on Weather Dataset with Stable Diffusion](notebooks/fastai_resnet34_test_weather.ipynb)
-   [ResNet50 Test on Weather Dataset with Stable Diffusion](notebooks/fastai_resnet50_test_weather.ipynb)
-   [ResNet34 Test on Comic Dataset with Stable Diffusion](notebooks/fastai_resnet34_test_comic.ipynb)
-   [ResNet50 Test on Comic Dataset with Stable Diffusion](notebooks/fastai_resnet50_test_comic.ipynb)
-   [ResNet34 Test on Small Indoor Dataset with DALLE2](notebooks/fastai_resnet34_test_dalle2_small_indoor.ipynb)
-   [ResNet50 Test on Small Indoor Dataset with DALLE2](notebooks/fastai_resnet50_test_dalle2_small_indoor.ipynb)
-   [ResNet34 Test on Weather Dataset with DALLE2](notebooks/fastai_resnet34_test_dalle2_weather.ipynb)
-   [ResNet50 Test on Weather Dataset with DALLE2](notebooks/fastai_resnet50_test_dalle2_weather.ipynb)

## License

[MIT](LICENSE)
