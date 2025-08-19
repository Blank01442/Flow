@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "FLOW_DIR=C:\Users\Administrator\Desktop\Flow"
set "CURRENT_DIR=%CD%"
cd /d "%FLOW_DIR%"
set "ARGS="
:process_args
if "%1"=="" goto run_flow
set "ARG=%1"
if exist "%CURRENT_DIR%\%ARG%" (
    set "ARGS=%ARGS% "%CURRENT_DIR%\%ARG%""
) else (
    set "ARGS=%ARGS% %1"
)
shift
goto process_args
:run_flow
python -m flow.flow_cli %ARGS%