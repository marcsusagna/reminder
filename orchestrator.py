import subprocess
import time
import schedule

SERVER_PORT='8502'

def run_webapp():
    subprocess.Popen(
        ['streamlit', 'run', 'app.py', '--server.port',  SERVER_PORT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

def run_main():
    subprocess.run(['python', 'main.py'])

def schedule_tasks():
    schedule.every(5).seconds.do(run_main)

    while True:
        schedule.run_pending()
        time.sleep(1)

def run_reminders():
    run_webapp()
    schedule_tasks()

if __name__ == "__main__":
    run_reminders()