import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config as conf

def run_webapp():
    print("hello")
    subprocess.Popen(
        ['streamlit', 'run', 'app/app.py', '--server.port',  conf.SERVER_PORT],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

if __name__ == "__main__":
    run_webapp()