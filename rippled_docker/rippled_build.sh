#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o xtrace

./conan_install.sh

cmake -S ${SOURCE_DIR} \
    -B ${BUILD_DIR} \
    -DCMAKE_BUILD_TYPE=${CONFIG} \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_TOOLCHAIN_FILE:FILEPATH=/${BUILD_DIR}/build/generators/conan_toolchain.cmake

cmake --build "${BUILD_DIR}" --target rippled --parallel $NPROC
