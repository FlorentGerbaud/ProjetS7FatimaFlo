@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "arg1=2.0"
set "arg2=1.0"

:: Check if the first argument is provided and use it if available
if not "%~1"=="" set "arg1=%~1"

:: Check if the second argument is provided and use it if available
if not "%~2"=="" set "arg2=%~2"

:: Run the Python script with the provided or default arguments
python Modele1.py %arg1% %arg2%

:: Exit the batch script
exit /b
