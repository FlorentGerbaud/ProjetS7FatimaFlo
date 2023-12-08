@echo off
setlocal enabledelayedexpansion


set "lambda2=-20.0"
set "h=0.0001"
set "d2=1.0"
set "nameCase="Simulation of the Accordion Phenomenon""

if not "%~1"=="" set "lambda2=%~1"
if not "%~2"=="" set "h=%~2"
if not "%~3"=="" set "d2=%~3"
if not "%~4"=="" set "nameCase=%~4"

python ../../../../PythonFile/Model1W2C_Equilibrium_CV_DV.py %lambda2% %h% %d2% %nameCase%

exit /b
::pause