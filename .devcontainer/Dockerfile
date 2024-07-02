FROM python:3.12-slim

ARG USERNAME=user

USER root

RUN apt-get update -y \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y --no-install-recommends \
  locales \
  tzdata \
  git \
  ca-certificates \
  openssh-client \
  fontconfig \
  fonts-noto-cjk \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN locale-gen ja_JP.UTF-8 \
  && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV TZ=Asia/Tokyo \
  LANG=ja_JP.UTF-8 \
  LANGUAGE=ja_JP:jp \
  LC_ALL=ja_JP.UTF-8

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /workspaces

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN groupadd -r $USERNAME && useradd -r -g $USERNAME $USERNAME
RUN mkdir /home/$USERNAME && chown $USERNAME:$USERNAME /home/$USERNAME

USER $USERNAME

ENTRYPOINT [ "/bin/bash" ]
