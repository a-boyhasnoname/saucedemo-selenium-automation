#!/usr/bin/env bash
set -e
mkdir -p reports screenshots
python -m pytest --browser chrome --html=reports/report.html --self-contained-html
