@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=1.0"
set "h=1.0"
set "a3=1.0"
set "CaseToLaunch="Simulation of the Accordion Phenomenon with the third driver drunk""

if not "%~1"=="" set "a2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "a3=%~3"
if not "%~4"=="" set "CaseToLaunch=%~4"


python ../../../../../PythonFile/Model1W3C_O_Acc_D3.py %a2% %h% %a3% %CaseToLaunch%
exit /b