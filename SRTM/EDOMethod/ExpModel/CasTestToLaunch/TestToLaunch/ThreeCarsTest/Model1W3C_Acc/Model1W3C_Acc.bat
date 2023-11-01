@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=2.0"
set "h=1.0"
set "a3=1.3"
set "CaseToLaunch="Simulation of an Accident between two Cars""

if not "%~1"=="" set "a2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "a3=%~3"

python ../../../PythonFile/Model1W3C_Acc.py %a2% %h% %a3% %CaseToLaunch%
exit /b
