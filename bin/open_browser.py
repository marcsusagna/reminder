import subprocess

from config import SERVER_PORT, BROWSER_EXE_PATH


url = f"http://localhost:{SERVER_PORT}/"

subprocess.run([BROWSER_EXE_PATH, '--new-window', url])