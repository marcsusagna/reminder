@echo off
start cmd /k "powershell -ExecutionPolicy Bypass -File run_app_in_docker.ps1"
cd /d ".."
poetry install
timeout /t 5
start cmd /k "poetry run remind_me --seconds=900"