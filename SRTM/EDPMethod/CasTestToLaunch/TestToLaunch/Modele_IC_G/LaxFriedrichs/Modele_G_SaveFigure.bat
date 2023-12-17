@echo off
setlocal enabledelayedexpansion

set "nameCaseToLaunch=LF"
set "isSaveFigure=1"

if not "%~1"=="" set "nameCaseToLaunch=%~1"
if not "%~2"=="" set "isSaveFigure=%~2"

python ../../../PythonFile/Modele_G.py !nameCaseToLaunch! !isSaveFigure!

exit /b
::pause
