# reminder
Triggers alerts to correct posture during desk time when working on Windows. It starts an app hosting the message and a client regularly opening a browser towards the app. 

Can run in these three setups:
- WSL: Both App and client run on WSL. Client leverages Windows browser
- Windows: Both app and client runs on windows directly
- Docker ("detached"): App runs on a docker container while client runs on windows directly

## Running on WSL:

Steps:
- Clone this repo into your linux workspace within WSL
- Ensure config.py BROWSER_LINUX_EXE_PATH points to the path of your Windows browser from WSL 
- modify wsl_run_reminders.bat to point path resolution towards this repository directory 
- ensure poetry is installed in WSL and executable (in PATH)
- From windows, navigate to the linux workspace where you have this repository and execute scripts/wsl_run_reminders.bat (double click)

## Running on Windows

Steps:
- Clone this repo into your Windows workspace (your user folder)
- Ensure config.py BROWSER_WIN_EXE_PATH points to the path of your Windows browser
- modify windows_run_reminders.bat to point path resolution towards this repository directory (uses cd .. as it assumes it is executed from where it is)
- ensure poetry is installed in Windows and executable (in PATH)
- From windows, navigate to the Windows workspace where you have this repository and execute scripts/windows_run_reminders.bat (double click)

## Running app on Docker and client on Windows

Steps:
- Clone this repo into your Windows workspace (your user folder)
- Ensure config.py BROWSER_WIN_EXE_PATH points to the path of your Windows browser
- modify docker_run_reminders.bat to point path resolution towards this repository directory (uses cd .. as it assumes it is executed from where it is)
- ensure poetry is installed in Windows and executable (in PATH)
- Open Docker Desktop and make sure you can execute docker commands from powershell / command prompt
- From windows, navigate to the Windows workspace where you have this repository and execute scripts/docker_run_reminders.bat (double click)


