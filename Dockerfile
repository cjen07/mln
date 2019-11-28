FROM ubuntu:18.04

WORKDIR /home
# if not in China, you can delete the following two lines
COPY ./sources.list.163 ./sources.list.163
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && mv sources.list.163 /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo curl zsh wget git tmux vim build-essential python3-pip

RUN git clone https://github.com/danielnyga/pracmln
WORKDIR /home/pracmln
RUN git checkout tags/1.2.4
RUN python3 setup.py install
RUN python3 -m pip install --upgrade pip
RUN pip install pyparsing dnutils psutil numpy scipy mpmath

WORKDIR /home
RUN git clone --branch 1.0.1 --depth 1 https://github.com/toulbar2/toulbar2.git

WORKDIR /home/toulbar2
COPY ./install.sh ./install.sh
RUN sh ./install.sh

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y python3-tk

WORKDIR /home

CMD ["/bin/bash"]