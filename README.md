# reminder
Triggers alerts to correct posture during desk time when working on Windows. It starts an app hosting the message and a client regularly opening a browser towards the app. 

Can run in these three setups:
- WSL: See scripts/wsl_run_reminder.bat. Modify paths accordingly to point to this repository within your WSL distribution. Run script from its location (within WSL)
- Directly on windows: See scripts/windows_run_reminder.bat
- Docker: See scripts/run_docker.sh

## Running on WSL:

Steps:
- Clone this repo into your linux workspace within WSL
- Ensure config.py BROWSER_LINUX_EXE_PATH points to the path of your Windows browser from WSL 
- modify wsl_run_reminders.bat to point path resolution towards this repository directory 
- ensure poetry is installed in WSL and executable (in PATH)
- From windows, navigate to the linux workspace where you have this repository and execute scripts/wsl_run_reminders.bat (double click)




