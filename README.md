# crawler

# 環境設定

#### 安裝 pipenv

    pip install pipenv==2022.4.8

#### 安裝 repo 套件

    pipenv sync

#### 建立環境變數

    ENV=DEFAULT python genenv.py
    ENV=DOCKER python genenv.py
    ENV=PRODUCTION python genenv.py

#### 排版

    black -l 80 crawler/

# Worker

#### 啟動預設執行 celery 的 queue 的工人

    pipenv run celery -A crawler.worker worker --loglevel=info

#### 啟動執行 twse 的 queue 的工人

    pipenv run celery -A crawler.worker worker -Q twse,tpex --loglevel=info

# Producer

#### 發送任務

    pipenv run python crawler/producer.py

#### for loop 發送多個任務

    pipenv run python crawler/producer_crawler_finmind.py

#### 發送任務到不同 queue

    pipenv run python crawler/producer_multi_queue.py


# Docker

#### build docker image

    docker build -f Dockerfile -t linsamtw/tibame_crawler:0.0.1 .

#### push docker image

    docker push linsamtw/tibame_crawler:0.0.1

#### 建立 network

    docker network create my_network

#### 啟動 rabbitmq

    docker compose -f rabbitmq-network.yml up -d

#### 關閉 rabbitmq

    docker compose -f rabbitmq-network.yml down

#### 啟動 worker

    docker compose -f docker-compose-worker-network.yml up -d

#### 查看 docker container 狀況

    docker ps -a

#### 查看 log

    docker logs container_name


