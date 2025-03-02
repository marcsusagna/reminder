@echo off
wsl bash -c "echo 'Hi, your reminders are running!' && source ~/.profile && cd reminder && poetry install && poetry run remind_me"
