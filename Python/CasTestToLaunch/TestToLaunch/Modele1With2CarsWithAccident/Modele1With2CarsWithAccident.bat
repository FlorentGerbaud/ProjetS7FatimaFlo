@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=1.75"
set "h=1.5"

:: Check if the first argument is provided and use it if available
if not "%~1"=="" set "a2=%~1"

:: Check if the second argument is provided and use it if available
if not "%~2"=="" set "h=%~2"

:: Run the Python script with the provided or default arguments
python ../../PythonFile/Modele1LaunchTest.py %a2% %h%

:: Exit the batch script
exit /b
