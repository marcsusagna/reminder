import subprocess
import time
import schedule

from config import SERVER_PORT

def run_webapp():
    subprocess.Popen(
        ['streamlit', 'run', 'app/app.py', '--server.port',  SERVER_PORT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def run_open_browser():
    subprocess.run(['python', 'bin/open_browser.py'])

def schedule_tasks():
    schedule.every(5).seconds.do(run_open_browser)

    while True:
        schedule.run_pending()
        time.sleep(1)

def run_reminders():
    run_webapp()
    schedule_tasks()

if __name__ == "__main__":
    run_reminders()