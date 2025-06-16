call C:/ProgramData/Anaconda3/Scripts/activate.bat
call conda activate qcodespp-docs
call cd C:/git/qcodespp.github.io
call python autoconf.py
call sphinx-build -M html docs/source docs/build
call python autorename.py
call python autoconf.py