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

## Make Dataset

### Download raw dataset and extract it

A shell script is provided to download and extract the raw dataset. The script will download the raw dataset to `dataset/raw` directory.

```bash
./dataset/download_indoor.sh
```

### Run `dataset_factory` to process raw dataset

```bash
./dataset_factory
```

or

```bash
./dataset_factory -d dataset/raw -o dataset/processed -s 256
```

The processed dataset will be saved to `dataset/processed` folder.
