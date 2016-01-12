FROM ubuntu:14.04
MAINTAINER Jacky Zhu <ztbjdx@163.com>

CMD echo executing CMD

ENV IMAGE_VERSION jacky_v1.0

RUN apt-get update \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    vim \
    git \
    python-pip \
    python2.7-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/tools/go \
    && curl -sSL https://storage.googleapis.com/golang/go1.5.2.linux-amd64.tar.gz | tar -v -C /opt/tools/go -xz --strip-components 1 \
    && mkdir -p /opt/workspace/go

ENV GOROOT /opt/tools/go
ENV GOPATH /opt/workspace/go
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/tools/go/bin

EXPOSE 8000
#ADD vimrc /root/.vimrc
