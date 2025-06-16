FROM ubuntu:20.04

# 更新套件列表並安裝 Python 3.8 和 pip
RUN apt-get update && \
    apt-get install python3.8 -y && \
    apt-get install python3-pip -y

RUN pip install pipenv==2022.4.8

RUN mkdir /crawler
COPY ./crawler /crawler/
COPY ./setup.py /crawler/
WORKDIR /crawler/

RUN pipenv sync

# # env
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["/bin/bash"]
