@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=2.0"
set "h=1.0"
set "a3=1.0"
set "CaseToLaunch="Simulation of the Accordion Phenomenon""

if not "%~1"=="" set "a2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "a3=%~3"
if not "%~4"=="" set "CaseToLaunch=%~4"


python ../../../PythonFile/Modele1W3Cars_Aco.py %a2% %h% %a3% %CaseToLaunch%
exit /b