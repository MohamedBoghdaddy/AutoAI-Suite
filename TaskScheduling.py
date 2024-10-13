import schedule
import time

def job():
    print("Task executed")

schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
