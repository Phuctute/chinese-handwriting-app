# Script khởi chạy ứng dụng trên Windows PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Set-Location -Path $PSScriptRoot

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  KHỞI ĐỘNG ỨNG DỤNG CHÉP TAY TIẾNG TRUNG PHỒN THỂ" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Đang khởi chạy máy chủ cục bộ và mở trình duyệt..." -ForegroundColor Yellow

python server.py
