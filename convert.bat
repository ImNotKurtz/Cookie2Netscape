@echo off
title Cookie2Netscape - H4CK3R M0D3
color 0A
cls

echo.
echo ===================================================
echo  ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗███████╗███████╗
echo ██╔══██╗██╔═══██╗██╔═══██╗██║  ██║██║██╔════╝██╔════╝
echo ██████╔╝██║   ██║██║   ██║███████║██║███████╗█████╗  
echo ██╔═══╝ ██║   ██║██║   ██║██╔══██║██║╚════██║██╔══╝  
echo ██║     ╚██████╔╝╚██████╔╝██║  ██║██║███████║███████╗
echo ╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
echo.
echo            C O O K I E  2  N E T S C A P E
echo ===================================================
echo.
echo [*] Starting cookie conversion...
echo.

cd /d "%~dp0"
python convert.py

echo.
echo [✅] Process completed!
pause
