@echo off
wsl bash -c "echo 'Hi, your reminders are running!' && source ~/.profile && cd reminder && poetry run python3 orchestrator.py"
