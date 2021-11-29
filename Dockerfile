FROM centos:7
#install java
RUN yum -y update
RUN yum -y remove java
RUN yum install -y \
       java-11-openjdk \
       java-11-openjdk-devel
#install python
RUN yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel make -y wget unzip

RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz\
&& tar -zxvf Python-3.7.0.tgz\
&& cd Python-3.7.0\
&& ./configure\
&& make&&make install


WORKDIR /Ghidra
COPY requirement.txt /Ghidra/
RUN pip3 install --upgrade pip peid
RUN pip install -r requirement.txt

COPY ghidra_10.0.4_PUBLIC_20210928.zip /Ghidra/
RUN unzip ghidra_10.0.4_PUBLIC_20210928.zip
