:: containe the build instruction
:: a "main" folder should be created into the src directory


:: Generator directory
set Generator= Generator

echo %Generator%
cd %Generator%
.\Gen.py
cd ..

if exist src\main\ rmdir src\main /S /Q >> .log

if exist %Generator%\main\ xcopy %Generator%\main\ src\main\ /E >> .log
echo python generation completed successfully
