# Install CodeX package in editable mode and capture the output
Write-Host "Installing CodeX CLI and extracting exact path..." -ForegroundColor Cyan
$pipOutput = (pip install -e . 2>&1 | Out-String)
Write-Host $pipOutput

# Extract the exact path from pip's warning message
if ($pipOutput -match "'(.*?\\Scripts)'") {
    $pythonScriptsPath = $matches[1]
    Write-Host "Exact Python Scripts directory detected at: $pythonScriptsPath" -ForegroundColor Yellow

    # Get the current User PATH environment variable
    $userPath = [Environment]::GetEnvironmentVariable("PATH", "User")

    # Check if the Scripts path is already in the User PATH
    if ($userPath -split ';' -contains $pythonScriptsPath) {
        Write-Host "The Python Scripts directory is already in your PATH." -ForegroundColor Green
    } else {
        Write-Host "Adding Python Scripts to your User PATH..." -ForegroundColor Yellow
        # Add the path to the User PATH
        $newPath = "$userPath;$pythonScriptsPath"
        [Environment]::SetEnvironmentVariable("PATH", $newPath, "User")
        
        # Also update the current session PATH so it works immediately
        $env:PATH = "$env:PATH;$pythonScriptsPath"
        Write-Host "Successfully added to PATH!" -ForegroundColor Green
    }
} else {
    Write-Host "Could not automatically detect the Scripts directory from pip's output. It may already be in your PATH." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "CodeX installation complete! It is now available globally." -ForegroundColor Green
Write-Host "You can now run:" -ForegroundColor White
Write-Host "  codex `"list files in this directory`"" -ForegroundColor Yellow
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "NOTE: To use 'codex' as a CLI tool globally in a new window, just close and reopen your terminal." -ForegroundColor Red
