import subprocess

url = "http://localhost:8502/"
chrome_path = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"

subprocess.run([chrome_path, '--new-window', url])