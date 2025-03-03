@echo off
start cmd /k wsl bash -c "echo 'Starting app' && cd .. && poetry install && poetry run start_app"
timeout /t 5
start cmd /k wsl bash -c "echo 'Running reminders' && cd .. && poetry run remind_me --seconds=5"