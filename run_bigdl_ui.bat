echo using %1
cd /d %~dp0
call "C:\Program Files (x86)\Intel\oneAPI\setvars.bat"

python demo.py