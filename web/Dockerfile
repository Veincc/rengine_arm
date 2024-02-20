# Base image
FROM ubuntu:22.04
# Change apt source
RUN sed -i 's/http:\/\/archive.ubuntu.com/http:\/\/mirrors.aliyun.com/g' /etc/apt/sources.list

# Labels and Credits
LABEL \
    name="reNgine" \
    author="Yogesh Ojha <yogesh.ojha11@gmail.com>" \
    description="reNgine is a automated pipeline of recon process, useful for information gathering during web application penetration testing."

# Source url
#ARG GITLAB=

# Environment Variables
ENV DEBIAN_FRONTEND="noninteractive" \
    DATABASE="postgres"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GOROOT="/usr/local/go"
ENV GOPATH=$HOME/go
ENV PATH="${PATH}:${GOROOT}/bin:${GOPATH}/bin"

# Install Python
RUN apt update -y && \
    apt update -y && \
    apt install -y \
    python3.10 \
    python3-dev \
    python3-pip

# Install essential packages
RUN apt install -y  --no-install-recommends \
    build-essential \
    cmake \
    geoip-bin \
    geoip-database \
    gcc \
    git \
    libpq-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libpcap-dev \
    netcat \
    nmap \
    x11-utils \
    xvfb \
    wget \
    unzip \
    curl \
    python3-netaddr \
    software-properties-common

# Get Xray
#ARG XRAY_VERSION=1.9.11
#RUN wget https://github.com/chaitin/xray/releases/download/${XRAY_VERSION}/xray_linux_amd64.zip \
#    && unzip xray_linux_amd64.zip \
#    && mkdir /usr/src/github/ \
#    && mkdir /usr/src/github/xray/ \
#    && mv xray_linux_amd64 /usr/src/github/xray/xray \
#    && rm xray_linux_amd64.zip \
#    && chmod +x /usr/src/github/xray/xray \
## Generate xray.yaml/module.xray.yaml/plugin.xray.yaml
#    && /usr/src/github/xray/xray \
## Generate default configurations to config.yaml
#    && /usr/src/github/xray/xray

RUN add-apt-repository ppa:mozillateam/ppa

# Download and install go 1.20
RUN wget https://mirrors.aliyun.com/golang/go1.21.4.linux-amd64.tar.gz \
    && tar -xvf go1.21.4.linux-amd64.tar.gz \
    && rm go1.21.4.linux-amd64.tar.gz \
    && mv go /usr/local

# Download geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz \
    && tar -xvf geckodriver-v0.32.0-linux64.tar.gz \
    && rm geckodriver-v0.32.0-linux64.tar.gz \
    && mv geckodriver /usr/bin

# Make directory for app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add Proxy
RUN go env -w GO111MODULE=on \
    && go env -w GOPROXY=https://goproxy.cn,direct \
# Download Go packages
#    && go install -v -v github.com/bp0lr/gauplus@latest \
#    && go install -v github.com/jaeles-project/gospider@latest \
#    && go install -v github.com/tomnomnom/gf@latest \
#    && go install -v github.com/tomnomnom/unfurl@latest \
    && go install -v github.com/tomnomnom/waybackurls@latest \
    && go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest \
    && go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest \
    && go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest \
    && go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest \
#    && go install -v github.com/hakluke/hakrawler@latest \
#    && go install -v github.com/lc/gau/v2/cmd/gau@latest \
#    && go install -v github.com/jaeles-project/gospider@latest \
    && go install -v github.com/owasp-amass/amass/v3/...@latest \
    && go install -v github.com/ffuf/ffuf@latest \
    && go install -v github.com/projectdiscovery/tlsx/cmd/tlsx@latest
#    && go install -v github.com/hahwul/dalfox/v2@latest \
#    && go install -v github.com/projectdiscovery/katana/cmd/katana@latest \
#    && go install -v github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest \
#    && go install -v github.com/sa7mon/s3scanner@latest

# Update Nuclei and Nuclei-Templates
RUN nuclei -update \
    && nuclei -update-templates

# Update project discovery tools
RUN httpx -up \
    && naabu -up \
    && subfinder -up \
    && tlsx -up \
#    && katana -up \

RUN ls
# Copy requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade setuptools pip && \
    pip3 install -r /tmp/requirements.txt \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

# install eyewitness

RUN python3 -m pip install fuzzywuzzy \
    selenium==4.9.1 \
    python-Levenshtein \
    pyvirtualdisplay \
    netaddr \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

# Copy source code
COPY . /usr/src/app/

# httpx seems to have issue, use alias instead!!!
RUN echo 'alias httpx="/go/bin/httpx"' >> ~/.bashrc
