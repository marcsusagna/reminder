import subprocess
import sys
import os
import time
import schedule

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config as conf

def run_webapp():
    subprocess.Popen(
        ['streamlit', 'run', 'app/app.py', '--server.port',  conf.SERVER_PORT],
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
    interval=int(sys.argv[1]) if len(sys.argv) > 1 else conf.DEFAULT_INTERVAL
    run_reminders(interval)