@echo off
:: modify path where the repository is
cd workspace\reminder && ^
poetry install && ^
poetry run remind_me
pause