@echo off
:: Assumes executed from scripts/ folder
cd .. && ^
poetry install && ^
poetry run remind_me