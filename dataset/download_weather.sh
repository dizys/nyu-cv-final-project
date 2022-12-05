#!/usr/bin/env bash

shell_dir=$(dirname "$0")
raw_dir=${shell_dir}/raw
download_dir=${shell_dir}/download

mkdir -p "${download_dir}"
rm -rf "${raw_dir}"

# Download the dataset
echo "Downloading the dataset..."
wget "https://github.com/dizys/nyu-cv-final-project/releases/download/raw-datasets/weather256.zip" -O "${download_dir}/weather256.zip"

mkdir -p "${download_dir}/weather256"

echo "Extracting the dataset..."
# Extract the dataset
unzip "${download_dir}/weather256.zip" -d "${download_dir}/weather256"

# Move the dataset to the raw directory
echo "Moving the dataset to the raw directory..."
mv "${download_dir}/weather256" "$raw_dir"

# Remove the downloaded file and the extracted folder
echo "Removing the downloaded file and the extracted folder..."
rm "${download_dir}/weather256.zip"
rm -rf "${download_dir}/weather256"

echo "- Done."
