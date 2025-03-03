import subprocess
import sys
import os
import time
import schedule

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config as conf

def run_open_browser():
    subprocess.run(['python3', 'bin/open_browser.py'])

def schedule_tasks(interval: int):
    schedule.every(interval).seconds.do(run_open_browser)

    while True:
        schedule.run_pending()
        time.sleep(1)

def main(interval):
    schedule_tasks(interval)

if __name__ == "__main__":
    interval=int(sys.argv[1]) if len(sys.argv) > 1 else conf.DEFAULT_INTERVAL
    main(interval)