@echo off
setlocal enabledelayedexpansion


set "lambda2=10.0"
set "h=1.0"
set "d2=1.0"

if not "%~1"=="" set "lambda2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "d2=%~3"

python ../../../PythonFile/Modele2W2C_Aco.py %lambda2% %h% %d2%

exit /b
::pause