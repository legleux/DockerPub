ARG DIST_TAG=18.04

FROM ubuntu:$DIST_TAG AS conan_build
ARG SOURCE_DIR=rippled
ARG BUILD_DIR=build

COPY rippled_docker/build_deps.sh .
RUN ./build_deps.sh && rm build_deps.sh

COPY rippled_docker/cmake_conan_setup.sh .

RUN ./cmake_conan_setup.sh && rm cmake_conan_setup.sh

COPY rippled_docker/enable_pyenv.sh .

COPY rippled_docker/conan_install.sh .
COPY rippled_docker/rippled_build.sh .

COPY ${SOURCE_DIR} /${SOURCE_DIR}

ARG BUILD_DIR=build
RUN cd ${SOURCE_DIR} && mkdir "${BUILD_DIR}"

ENV BUILD_DIR=${BUILD_DIR}
ENV SOURCE_DIR=${SOURCE_DIR}
ENV CONFIG=Release
ENV NPROC=30

RUN ./conan_install.sh

RUN ./rippled_build.sh

RUN strip ${BUILD_DIR}/rippled

FROM ubuntu:$DIST_TAG AS rippled
ARG BUILD_DIR=/build
ARG SOURCE_DIR=/rippled

COPY --from=conan_build ${BUILD_DIR}/rippled /opt/ripple/bin/rippled
COPY rippled_docker/entrypoint.sh .
COPY --from=conan_build ${SOURCE_DIR}/cfg/rippled-example.cfg /etc/opt/ripple/rippled.cfg
COPY --from=conan_build ${SOURCE_DIR}/cfg/validators-example.txt /etc/opt/ripple/validators.txt

ENTRYPOINT [ "/entrypoint.sh" ]
