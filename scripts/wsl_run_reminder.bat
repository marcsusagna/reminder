@echo off
start cmd /k wsl bash -c "echo 'Starting app' && cd ~/lx_workspace/reminder && poetry install && poetry run start_app"
timeout /t 5
start cmd /k wsl bash -c "echo 'Running reminders' && cd ~/lx_workspace/reminder && poetry run remind_me --seconds=5"