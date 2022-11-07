#!/usr/bin/env bash

shell_dir=$(dirname "$0")

mkdir -p "$shell_dir/raw"

# Download the dataset
wget "http://groups.csail.mit.edu/vision/LabelMe/NewImages/indoorCVPR_09.tar" -P "$shell_dir"

# Extract the dataset
tar -xvf indoorCVPR_09.tar -C "$shell_dir/raw"

# Remove the compressed file
rm "$shell_dir/indoorCVPR_09.tar"
