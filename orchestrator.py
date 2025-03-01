import subprocess
import time
import schedule

def run_webapp():
    subprocess.Popen(
        ['streamlit', 'run', 'app.py', '--server.port',  '8502'],
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

#def run_reminders():

if __name__ == "__main__":
    run_webapp()
    schedule_tasks()