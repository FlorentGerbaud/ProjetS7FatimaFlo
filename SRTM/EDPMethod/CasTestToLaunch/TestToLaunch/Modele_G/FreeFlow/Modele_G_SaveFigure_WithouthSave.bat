@echo off
setlocal enabledelayedexpansion

set "nameCaseToLaunch=FF"
set "isSaveFigure=0"

if not "%~1"=="" set "nameCaseToLaunch=%~1"
if not "%~2"=="" set "isSaveFigure=%~2"

python ../../../PythonFile/Modele_G.py !nameCaseToLaunch! !isSaveFigure!

exit /b
::pause
