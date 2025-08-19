@echo off
REM Flow Installation Script
REM This script installs Flow and sets up the 'flow' command

echo ====================================================
echo Flow Programming Language Installation
echo ====================================================

REM Get the directory where this script is located
set "INSTALL_DIR=%~dp0"
set "INSTALL_DIR=%INSTALL_DIR:~0,-1%"  REM Remove trailing backslash

echo Installing Flow from: %INSTALL_DIR%

REM Copy flow.bat to System32 (requires admin privileges)
echo Copying flow command to system directory...
copy "%INSTALL_DIR%\flow.bat" "C:\WINDOWS\system32\flow.bat" >nul

if %errorlevel% equ 0 (
    echo [SUCCESS] Flow command installed successfully!
) else (
    echo [ERROR] Failed to install flow command. You may need to run this script as Administrator.
    echo Please right-click on this script and select "Run as administrator"
    pause
    exit /b 1
)

echo.
echo ====================================================
echo Installation Complete!
echo ====================================================
echo You can now run Flow programs using:
echo.
echo    flow program.flow
echo.
echo Examples:
echo    flow examples\hello.flow
echo    flow examples\fibonacci.flow --profile
echo.
echo The Flow command is now available from any directory.
echo.
pause