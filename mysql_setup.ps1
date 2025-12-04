# MySQL Setup Guide for Nuclear Magic Numbers Project
# ===================================================

Write-Host "MySQL Database Setup Complete!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "MySQL Version: 8.4.6" -ForegroundColor Yellow
Write-Host "Installation Path: C:\Program Files\MySQL\MySQL Server 8.4" -ForegroundColor Yellow
Write-Host "Data Directory: $env:USERPROFILE\mysql-data" -ForegroundColor Yellow
Write-Host ""

Write-Host "Database Created: nuclear_physics" -ForegroundColor Green
Write-Host "Root Password: password123" -ForegroundColor Red
Write-Host ""

Write-Host "To connect to MySQL:" -ForegroundColor Cyan
Write-Host "mysql -u root -p" -ForegroundColor White
Write-Host "Password: password123" -ForegroundColor White
Write-Host ""

Write-Host "To start MySQL server manually:" -ForegroundColor Cyan
Write-Host "Start-Process 'C:\Program Files\MySQL\MySQL Server 8.4\bin\mysqld.exe' -ArgumentList '--datadir=$env:USERPROFILE\mysql-data' -NoNewWindow" -ForegroundColor White
Write-Host ""

Write-Host "Sample data in nuclear_physics.magic_numbers table:" -ForegroundColor Cyan
& "C:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe" -u root -ppassword123 -e "USE nuclear_physics; SELECT * FROM magic_numbers;"

Write-Host ""
Write-Host "MySQL is ready for your nuclear physics data analysis!" -ForegroundColor Green