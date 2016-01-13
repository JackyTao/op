#!/bin/bash

apt-get update \
    && sudo apt-get install -y \
    build-essential \
    ca-certificates \
    curl \
    vim \
    git \
    python-pip \
    python2.7-dev \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

sudo mkdir -p /opt/tools/go \
    && sudo curl -sSL https://storage.googleapis.com/golang/go1.5.2.linux-amd64.tar.gz \
    | sudo tar -v -C /opt/tools/go -xz --strip-components 1 \
    && sudo mkdir -p /opt/workspace/go


echo '# --- configure from initdev.sh ---' >> ~/.bashrc
echo 'export GOROOT=/opt/tools/go' >> ~/.bashrc
echo 'export GOPATH=/opt/workspace/go' >> ~/.bashrc
echo 'export PATH=$PATH:/opt/tools/go/bin' >> ~/.bashrc
