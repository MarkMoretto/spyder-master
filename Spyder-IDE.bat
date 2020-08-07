@ECHO OFF

SETLOCAL

SET PATH=%CD%\venv;%PATH%
SET "pyexe=%CD%\venv\Scripts\python.exe"

%pyexe% bootstrap.py
