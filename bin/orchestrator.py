import subprocess
import sys
import time
import schedule

from config import SERVER_PORT, DEFAULT_INTERVAL

def run_webapp():
    subprocess.Popen(
        ['streamlit', 'run', 'app/app.py', '--server.port',  SERVER_PORT, '> /dev/null'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def run_open_browser():
    subprocess.run(['python', 'bin/open_browser.py'])

def schedule_tasks(interval: int):
    schedule.every(interval).seconds.do(run_open_browser)

    while True:
        schedule.run_pending()
        time.sleep(1)

def run_reminders(interval):
    run_webapp()
    schedule_tasks(interval)

if __name__ == "__main__":
    interval=int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INTERVAL
    run_reminders(interval)