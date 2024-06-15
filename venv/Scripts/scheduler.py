import schedule
import time
import subprocess

def run_etl_job():
    subprocess.run(["python", "scripts/run_etl.py"])

# Schedule the job every day at midnight
schedule.every().day.at("00:00").do(run_etl_job)

while True:
    schedule.run_pending()
    time.sleep(1)
