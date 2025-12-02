# ========================================
#  GITHUB PUBLICATION SCRIPT
#  Nuclear Magic Numbers Pattern
# ========================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  GITHUB PUBLICATION - Nuclear Magic Numbers Pattern" -ForegroundColor Yellow
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if we are in the correct directory
$currentPath = Get-Location
if ($currentPath.Path -notlike "*nuclear-magic-numbers-pattern*") {
    Write-Host "WARNING: You are not in the project directory!" -ForegroundColor Red
    Write-Host "Run this script from inside: nuclear-magic-numbers-pattern\" -ForegroundColor Yellow
    Write-Host "`nDo you want to continue anyway? (Y/N): " -ForegroundColor Yellow -NoNewline
    $response = Read-Host
    if ($response -ne "Y" -and $response -ne "y") {
        Write-Host "`nOperation cancelled.`n" -ForegroundColor Red
        exit
    }
}

# Check if Git is installed
$gitInstalled = $null
try {
    $gitVersion = git --version 2>$null
    $gitInstalled = $true
    Write-Host "   OK Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    $gitInstalled = $false
    Write-Host "   WARNING: Git is not installed!" -ForegroundColor Red
    Write-Host "   Please install Git first:" -ForegroundColor Yellow
    Write-Host "   1. Download from: https://git-scm.com/download/win" -ForegroundColor White
    Write-Host "   2. Install with default settings" -ForegroundColor White
    Write-Host "   3. Restart PowerShell and run this script again" -ForegroundColor White
    Write-Host ""
    Write-Host "   Or install via winget:" -ForegroundColor Yellow
    Write-Host "   winget install --id Git.Git -e --source winget" -ForegroundColor White
    Write-Host ""
    Write-Host "   Do you want to continue anyway to see the project structure? (Y/N): " -ForegroundColor Yellow -NoNewline
    $response = Read-Host
    if ($response -ne "Y" -and $response -ne "y") {
        Write-Host "`nOperation cancelled. Please install Git and try again.`n" -ForegroundColor Red
        exit
    }
    Write-Host "   Continuing without Git operations..." -ForegroundColor Yellow
    Write-Host ""
}
Write-Host "Step 1: Verifying files..." -ForegroundColor Cyan
$fileCount = (Get-ChildItem -Recurse -File).Count
Write-Host "   OK $fileCount files found" -ForegroundColor Green
Write-Host ""

# Step 2: Initialize Git
Write-Host "Step 2: Initializing Git repository..." -ForegroundColor Cyan
if ($gitInstalled) {
    if (Test-Path ".git") {
        Write-Host "   WARNING: Git repository already exists" -ForegroundColor Yellow
        Write-Host "   Do you want to reinitialize? (Y/N): " -ForegroundColor Yellow -NoNewline
        $response = Read-Host
        if ($response -eq "Y" -or $response -eq "y") {
            Remove-Item -Recurse -Force .git
            git init
            Write-Host "   OK Repository reinitialized" -ForegroundColor Green
        }
    } else {
        git init
        Write-Host "   OK Repository initialized" -ForegroundColor Green
    }
} else {
    Write-Host "   SKIPPED: Git not installed" -ForegroundColor Yellow
}
Write-Host ""

# Step 3: Add files
Write-Host "Step 3: Adding files to Git..." -ForegroundColor Cyan
if ($gitInstalled) {
    git add .
    Write-Host "   OK All files added" -ForegroundColor Green
} else {
    Write-Host "   SKIPPED: Git not installed" -ForegroundColor Yellow
}
Write-Host ""

# Step 4: Initial commit
Write-Host "Step 4: Creating initial commit..." -ForegroundColor Cyan
if ($gitInstalled) {
    git commit -m "Initial commit: Nuclear magic numbers phenomenological pattern - Complete recursive formula for magic numbers 2, 8, 20, 28, 50, 82, 126 - Prediction of 184 for superheavy elements - Full paper with LaTeX sources - Python calculator and visualization tools - Comprehensive documentation - Four major discoveries - MIT License"
    Write-Host "   OK Commit created successfully" -ForegroundColor Green
} else {
    Write-Host "   SKIPPED: Git not installed" -ForegroundColor Yellow
}
Write-Host ""

# Step 5: Configure remote
Write-Host "Step 5: Configuring remote repository..." -ForegroundColor Cyan
Write-Host "   Your GitHub username: AndreDionisio" -ForegroundColor Yellow
Write-Host "   Repository name: nuclear-magic-numbers-pattern" -ForegroundColor Yellow
Write-Host ""
if ($gitInstalled) {
    Write-Host "   IMPORTANT: You need to create the repository on GitHub first!" -ForegroundColor Yellow
    Write-Host "   Go to: https://github.com/new" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   Have you already created the repository on GitHub? (Y/N): " -ForegroundColor Yellow -NoNewline
    $response = Read-Host

    if ($response -eq "Y" -or $response -eq "y") {
        $remoteUrl = "https://github.com/AndreDionisio/nuclear-magic-numbers-pattern.git"
        
        # Remove existing remote if any
        git remote remove origin 2>$null
        
        git remote add origin $remoteUrl
        Write-Host "   OK Remote configured: $remoteUrl" -ForegroundColor Green
        Write-Host ""
        
        # Step 6: Push
        Write-Host "Step 6: Pushing to GitHub..." -ForegroundColor Cyan
        Write-Host "   Do you want to push now? (Y/N): " -ForegroundColor Yellow -NoNewline
        $response = Read-Host
        
        if ($response -eq "Y" -or $response -eq "y") {
            git branch -M main
            git push -u origin main
            Write-Host "   OK Push completed successfully!" -ForegroundColor Green
            Write-Host ""
            Write-Host "========================================" -ForegroundColor Cyan
            Write-Host "  SUCCESS! Repository published on GitHub" -ForegroundColor Green
            Write-Host "========================================" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "Access your repository at:" -ForegroundColor Yellow
            Write-Host "   https://github.com/AndreDionisio/nuclear-magic-numbers-pattern" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "Next steps:" -ForegroundColor Yellow
            Write-Host "   1. Add topics on GitHub" -ForegroundColor White
            Write-Host "   2. Create Release v1.0.0" -ForegroundColor White
            Write-Host "   3. Share on social networks" -ForegroundColor White
            Write-Host "   4. Submit paper to arXiv with GitHub link" -ForegroundColor White
            Write-Host ""
        } else {
            Write-Host "   Push cancelled. Execute manually:" -ForegroundColor Yellow
            Write-Host "   git branch -M main" -ForegroundColor White
            Write-Host "   git push -u origin main" -ForegroundColor White
            Write-Host ""
        }
    } else {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host "  PAUSED - Configure GitHub first" -ForegroundColor Yellow
        Write-Host "========================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Steps to create repository on GitHub:" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "1. Go to: https://github.com/new" -ForegroundColor White
        Write-Host "2. Fill in:" -ForegroundColor White
        Write-Host "   - Repository name: nuclear-magic-numbers-pattern" -ForegroundColor White
        Write-Host "   - Description: Phenomenological recursive formula for nuclear magic numbers" -ForegroundColor White
        Write-Host "   - Visibility: Public" -ForegroundColor White
        Write-Host "   - DO NOT check 'Add README'" -ForegroundColor White
        Write-Host "3. Click 'Create repository'" -ForegroundColor White
        Write-Host ""
        Write-Host "4. Then, run this script again" -ForegroundColor White
        Write-Host ""
    }
} else {
    Write-Host "   SKIPPED: Git operations not available" -ForegroundColor Yellow
    Write-Host "   To publish on GitHub:" -ForegroundColor Yellow
    Write-Host "   1. Install Git from: https://git-scm.com/download/win" -ForegroundColor White
    Write-Host "   2. Create repository on GitHub" -ForegroundColor White
    Write-Host "   3. Run: git init && git add . && git commit -m 'Initial commit' && git remote add origin <url> && git push -u origin main" -ForegroundColor White
    Write-Host ""
}Write-Host "========================================" -ForegroundColor Cyan