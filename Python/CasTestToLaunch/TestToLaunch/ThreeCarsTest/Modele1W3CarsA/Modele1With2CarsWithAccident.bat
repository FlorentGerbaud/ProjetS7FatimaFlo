@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=2.0"
set "h=1.0"
set "a3=1.0"

if not "%~1"=="" set "a2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "a3=%~3"

:: Run the Python script with the provided or default arguments
python ../../../PythonFile/Modele1Launch3Voitures.py %a2% %h% %a3%

:: Exit the batch script
exit /b
