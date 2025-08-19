@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
echo Installing Flow from: %SCRIPT_DIR%
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
echo Installation Complete!
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