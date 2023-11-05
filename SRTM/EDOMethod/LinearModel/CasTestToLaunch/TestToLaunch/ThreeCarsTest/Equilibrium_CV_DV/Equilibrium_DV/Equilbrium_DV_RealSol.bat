@echo off
setlocal enabledelayedexpansion

:: Set default values for the arguments
set "a2=-2.0"
set "h=0.0001"
set "isRealistic=0"

if not "%~1"=="" set "a2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "isRealistic=%~3"

python ../../../../PythonFile/Model1W2C_Equilibrium_CV_DV.py %a2% %h% %isRealistic%
exit /b
::pause