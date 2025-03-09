import subprocess
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config as conf

url = f"http://localhost:{conf.SERVER_PORT}/"

if sys.platform=='win32':
    browser_exe=conf.BROWSER_WIN_EXE_PATH
elif sys.platform=='linux':
    browser_exe=conf.BROWSER_LINUX_EXE_PATH
else:
    raise Exception('App is intended to run on windows or linux container/wsl in windows')

if __name__ == "__main__":
    subprocess.run([browser_exe, '--new-window', url])