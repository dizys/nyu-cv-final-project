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

We custom built the dataset ourselves from existing public real-photo datasets. We used Stable-Diffusion-based image-to-image model to generate images from real photos. This way, we ended up with a labeled dataset of real photos and generated photos. Learn how to build the dataset from [dataset/README.md](dataset/README.md).

## License

[MIT](LICENSE)
