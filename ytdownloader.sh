#!/bin/bash

# Mendapatkan path skrip
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Mendapatkan path proyek absolut dari skrip
PROJECT_DIR="/media/ario/HDD/koding/Desktop_Apps/python/yt_downloader/v1"

# Mengaktifkan virtual environment
source "$PROJECT_DIR/.venv/bin/activate"

# Menjalankan Jupyter Lab
python3 main.py

