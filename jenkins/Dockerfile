FROM jenkins/jenkins:lts
USER root


RUN apt-get update && \
apt-get install -qy \
  apt-utils \
  libyaml-dev \
  build-essential \
  python-dev \
  libxml2-dev \
  libxslt-dev \
  libffi-dev \
  libssl-dev \
  default-libmysqlclient-dev \
  python-mysqldb \
  python-pip \
  libjpeg-dev \
  zlib1g-dev \
  libblas-dev\
  liblapack-dev \
  libatlas-base-dev \
  apt-transport-https \
  ca-certificates \
  wget \
  software-properties-common \
  zip \
  unzip \
  gfortran && \
rm -rf /var/lib/apt/lists/*

# Install docker
RUN wget https://download.docker.com/linux/debian/gpg && \
    apt-key add gpg && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee -a /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -qy docker-ce

# Install compose
RUN curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN chmod 777 /usr/local/bin/docker-compose

RUN pip install cffi --upgrade
RUN pip install pip2pi ansible==2.0


# add the jenkins user to the docker group so that sudo is not required to run docker commands
RUN usermod -aG docker jenkins
RUN chown -R 1000 /var/jenkins_home

USER jenkins


