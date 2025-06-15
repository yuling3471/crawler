import pandas as pd
import requests

from crawler_sam.worker import app


# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler_finmind_upload2db():
    url = "https://api.finmindtrade.com/api/v4/data"
    token = ""  # 參考登入，獲取金鑰
    headers = {"Authorization": f"Bearer {token}"}
    parameter = {
        "dataset": "TaiwanStockInfo",
    }
    resp = requests.get(url, headers=headers, params=parameter)
    data = resp.json()
    df = pd.DataFrame(data["data"])


# 註冊 task, 有註冊的 task 才可以變成任務發送給 rabbitmq
@app.task()
def crawler(x):
    print("crawler")
    print("upload db")
    return x
