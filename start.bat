@echo off
chcp 65001 > nul
title Trình Giả Lập Chép Tay Tiếng Trung Phồn Thể
echo ==========================================================
echo   KHỞI ĐỘNG ỨNG DỤNG CHÉP TAY TIẾNG TRUNG PHỒN THỂ
echo ==========================================================
echo.
echo Đang mở server và trình duyệt...
echo.

cd /d "%~dp0"
python server.py

pause
