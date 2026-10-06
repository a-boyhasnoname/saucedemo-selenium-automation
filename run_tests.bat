@echo off
if not exist reports mkdir reports
if not exist screenshots mkdir screenshots
python -m pytest --browser chrome --html=reports/report.html --self-contained-html
pause
