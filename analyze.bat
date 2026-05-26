@echo off
if "%~1"=="/?" goto help
if /i "%~1"=="/help" goto help
if "%~1"=="-h" goto help
if "%~1"=="--help" goto help

set "arg=%~1"
set "arg=%arg:\=/%"

docker run --rm -v "%CD%:/app" -w /app python:3.11-slim python analyzer.py %arg%
goto end

:help
echo Usage: analyze.bat [path]
echo.
echo   (no argument)       Analyze all .txt files in sample_jobs/
echo   path/to/file.txt    Analyze a specific job description file
echo   path/to/directory   Analyze all .txt files in a directory
echo.
echo Requires Docker Desktop to be running.

:end
