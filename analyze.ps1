<#
.SYNOPSIS
    Analyze a job description against your skills.
.DESCRIPTION
    Runs the job description analyzer via Docker. Docker Desktop must be running.
.PARAMETER Path
    Path to a .txt file or a directory of .txt files. Defaults to sample_jobs/.
.PARAMETER Help
    Show this help message.
.EXAMPLE
    .\analyze.ps1
    Analyze all .txt files in sample_jobs/
.EXAMPLE
    .\analyze.ps1 path/to/job.txt
    Analyze a specific job description file.
.EXAMPLE
    .\analyze.ps1 path/to/directory
    Analyze all .txt files in a directory.
#>
param(
    [string]$Path,
    [switch]$Help
)

if ($Help -or $Path -eq '-h' -or $Path -eq '--help') {
    Write-Host "Usage: .\analyze.ps1 [path]"
    Write-Host ""
    Write-Host "  (no argument)       Analyze all .txt files in sample_jobs/"
    Write-Host "  path/to/file.txt    Analyze a specific job description file"
    Write-Host "  path/to/directory   Analyze all .txt files in a directory"
    Write-Host ""
    Write-Host "Requires Docker Desktop to be running."
    exit
}

$Path = $Path -replace '\\', '/'

docker run --rm `
    -v "${PWD}:/app" `
    -w /app `
    python:3.11-slim `
    python analyzer.py $Path
