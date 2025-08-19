@echo off
setlocal

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

REM Get the full path to the Flow installation (adjust this path as needed)
set "FLOW_DIR=C:\Users\Administrator\Desktop\Flow"

REM Save the current directory
set "CURRENT_DIR=%CD%"

REM Change to the Flow root directory
cd /d "%FLOW_DIR%"

REM Process arguments to handle file paths
set "ARGS="

:process_args
if "%1"=="" goto run_flow

REM Check if the argument is a file that exists in the current directory
set "ARG=%1"
if exist "%CURRENT_DIR%\%ARG%" (
    REM If it's a file in the current directory, use the full path
    set "ARGS=%ARGS% "%CURRENT_DIR%\%ARG%""
) else (
    REM Otherwise, use the argument as-is
    set "ARGS=%ARGS% %1"
)

shift
goto process_args

:run_flow
REM Run the Flow CLI with processed arguments
python -m flow.flow_cli %ARGS%