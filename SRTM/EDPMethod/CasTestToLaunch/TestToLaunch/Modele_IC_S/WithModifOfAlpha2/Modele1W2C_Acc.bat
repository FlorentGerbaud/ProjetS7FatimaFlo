@echo off
setlocal enabledelayedexpansion


set "lambda2=15.0"
set "h=1.0"
set "d2=1.0"
set "V2max=160.0"
set "nameCaseToLaunch="Accident due to Increasing of the acceleration of x2""

if not "%~1"=="" set "lambda2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "d2=%~3"
if not "%~4"=="" set "V2max=%~4"
if not "%~5"=="" set "nameCaseToLaunch=%~5"

python ../../../../PythonFile/Modele2W2C_Acc.py %lambda2% %h% %d2% %V2max% %nameCaseToLaunch%

exit /b
::pause