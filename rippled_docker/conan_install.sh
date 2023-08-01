#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o xtrace

. enable_pyenv.sh

conan export ${SOURCE_DIR}/external/snappy snappy/1.1.10@
conan export ${SOURCE_DIR}/external/soci soci/4.0.3@

conan install ${SOURCE_DIR}\
    --profile gcc \
    --output-folder ${BUILD_DIR} \
    --build missing \
    --settings build_type=${CONFIG}
