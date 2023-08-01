#!/usr/bin/env bash

echo "cd'ing into: ${SOURCE}"
cd ${SOURCE}
echo "Building in $PWD"

mkdir build
cp sample_program.sh build/sample_program.sh
echo "echo 'Built at: $(date)'" >> build/sample_program.sh
