:: conaine directive to Generate the mod
:: everything should be generated on run

cls

cd Python
call .\Gen.bat
cd ..
if exist MDK\src\main\ rmdir MDK\src\main /S /Q > .log
if exist Python\src\main\ move Python\src\main MDK\src >> .log

cls
echo build completed successfully !
