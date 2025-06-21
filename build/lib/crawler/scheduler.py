import time
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler

from crawler.tasks_crawler_finmind import crawler_finmind


def send_crawler_stock_price_task():
    # for 迴圈, 可一次發送多個任務
    for stock_id in ["2330", "0050", "2317", "0056", "00713"]:
        print(stock_id)
        crawler_finmind.delay(stock_id=stock_id)


def test_scheduler():
    print("========================test_scheduler=====================")


def main():
    scheduler = BackgroundScheduler(
        timezone="Asia/Taipei",
    )
    scheduler.add_job(
        id="test",
        func=test_scheduler,
        trigger="cron",
        hour="*",
        minute="*",
        day_of_week="*",
        second="*/5",
        coalesce=True,
    )
    scheduler.add_job(
        id="send_crawler_stock_price_task",
        func=send_crawler_stock_price_task,
        trigger="cron",
        hour="*/12",
        minute="0",
        day_of_week="*",
        second="0",
        coalesce=True,
    )
    print("send_crawler_stock_price_task add scheduler")
    scheduler.start()


if __name__ == "__main__":
    main()
    while True:
        time.sleep(600)
