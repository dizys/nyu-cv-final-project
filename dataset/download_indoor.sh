#!/usr/bin/env bash

shell_dir=$(dirname "$0")
raw_dir=${shell_dir}/raw
download_dir=${shell_dir}/download

mkdir -p "${download_dir}"
rm -rf "${raw_dir}"

# Download the dataset
print "Downloading the dataset..."
wget "http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar" -P "${download_dir}"

mkdir -p "${download_dir}/indoorCVPR_09"

print "Extracting the dataset..."
# Extract the dataset
tar -xvf "${download_dir}/indoorCVPR_09.tar" -C "${download_dir}/indoorCVPR_09"

# Move the dataset to the raw directory
print "Moving the dataset to the raw directory..."
mv "${download_dir}/indoorCVPR_09/Images/" "$raw_dir"

# Remove the downloaded file and the extracted folder
print "Removing the downloaded file and the extracted folder..."
rm "${download_dir}/indoorCVPR_09.tar"
rm -rf "${download_dir}/indoorCVPR_09"

print "- Done."
