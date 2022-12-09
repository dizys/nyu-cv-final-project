#!/usr/bin/env bash

shell_dir=$(dirname "$0")
raw_dir=${shell_dir}/raw
download_dir=${shell_dir}/download

mkdir -p "${download_dir}"
rm -rf "${raw_dir}"

# Download the dataset
echo "Downloading the dataset..."
wget -O "${download_dir}/comic_books_dataset.zip" "https://github.com/dizys/nyu-cv-final-project/releases/download/raw-datasets/comic_books_dataset.zip"

mkdir -p "${download_dir}/comic_books"

echo "Extracting the dataset..."
# Extract the dataset
unzip -qq "${download_dir}/comic_books_dataset.zip" -d "${download_dir}/comic_books"

# Move the dataset to the raw directory
echo "Moving the dataset to the raw directory..."
mv "${download_dir}/comic_books/" "$raw_dir"

# Remove the downloaded file and the extracted folder
echo "Removing the downloaded file and the extracted folder..."
rm "${download_dir}/comic_books_dataset.zip"

echo "- Done."
