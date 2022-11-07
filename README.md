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

## Make Dataset

### Download dataset

Indoor Scene Dataset: [Download](http://web.mit.edu/torralba/www/indoor.html)

### Extract dataset to `dataset/raw` folder

Put all the images in `dataset/raw` folder. The folder structure should retain the same as the original dataset.

### Run `dataset_factory`

```bash
./dataset_factory
```

or

```bash
./dataset_factory -d dataset/raw -o dataset/processed -s 256
```

The processed dataset will be saved to `dataset/processed` folder.
