@echo off
cd /d ".."
poetry install
start cmd /k "poetry run start_app"
timeout /t 5
start cmd /k "poetry run remind_me --seconds=900"