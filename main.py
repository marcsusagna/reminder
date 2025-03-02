import subprocess

SERVER_PORT='8502'

url = f"http://localhost:{SERVER_PORT}/"
chrome_path = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"

subprocess.run([chrome_path, '--new-window', url])