@echo off
call .\Gen.bat
if exist Build\ rmdir Build\ /S /Q >> .log
if exist MDK\build\libs\ xcopy MDK\build\libs\ Build\ /E >> .log
echo Build completed successfully
pause