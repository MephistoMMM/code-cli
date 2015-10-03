FROM phusion/baseimage
MAINTAINER Vangie Du from Coding IDE Team <duwan@coding.net>

EXPOSE 65210

# Custom sources.list
COPY sources.list /etc/apt/sources.list

# Update Base System
RUN apt-get update && apt-get -y upgrade


# Install chinese language support
# 这里需要 用 TERM xterm-256color
ENV TERM xterm
RUN apt-get install -y language-pack-zh-hans-base language-pack-zh-hant-base language-pack-en-base

ENV LC_ALL="en_US.UTF-8"
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US.UTF-8"
ENV VISUAL="vim"
ENV EDITOR="vim"

RUN echo "Asia/Shanghai" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata \
	&& locale-gen en_US.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

# Install Python &  Node.js & zsh & git & vim
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash - \
	&& apt-get install -y nodejs build-essential python \
		python-dev python-pip python-virtualenv wget git vim figlet fortune zsh


# Add user `coding`
RUN useradd --create-home --home-dir /home/coding --shell /usr/bin/zsh coding \
	&& echo "coding:coding" | chpasswd \
	&& adduser coding sudo \
	&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER coding
ENV HOME /home/coding

# Install oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
	&& cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
	&& printf '\nexport PATH="$HOME/.bin:$PATH"\nexport VISUAL="vim"\nexport EDITOR="vim"' \
	| tee -a ~/.bashrc >> ~/.zshrc

# Cleanup SSH

RUN sudo rm -rf /var/run/sshd \
	&& sudo rm -rf /etc/service/sshd \
	&& sudo rm -f /etc/ssh/sshd_config \
	&& sudo rm -f /etc/my_init.d/00_regen_ssh_host_keys.sh \
	&& sudo rm -rf /root/.ssh \
	&& sudo rm -f /etc/insecure_key* \
	&& sudo rm -f /usr/sbin/enable_insecure_key \
	&& sudo apt-get remove -y --purge openssh-server

USER root
ENV HOME /root

CMD ["/sbin/my_init"]

# codeVS: MpSSS <mephistommm@gmail.com>

# Add tool fpc
RUN mkdir /tmp/fpc
WORKDIR /tmp/fpc
RUN wget -O ./fpc.2.4.0.tar http://ncu.dl.sourceforge.net/project/freepascal/Linux/2.4.0/fpc-2.4.0.x86_64-linux.tar \
    && tar -xf ./fpc.2.4.0.tar\
    && ./install.sh -y \
    && cd .. \
    && rm -rf ./fpc

WORKDIR /tmp
ADD ./dist/ .


RUN cp -r /home/coding/.zshrc /home/coding/.oh-my-zsh /root/

CMD ["/usr/bin/zsh"]
