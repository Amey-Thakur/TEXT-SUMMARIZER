#!/bin/bash
set -e

echo "--------------------------------------------------"
echo "    TEXT SUMMARIZER - PythonAnywhere Setup        "
echo "--------------------------------------------------"

# 1. Create a Virtual Environment
echo "[1/4] Creating Virtual Environment..."
mkvirtualenv --python=/usr/bin/python3.10 myenv_${RANDOM} || { echo "Note: If mkvirtualenv failed, you might already be in an env. Proceeding..."; }

# 2. Install Dependencies (Optimized for space)
echo "[2/4] Installing libraries..."
rm -rf ~/.cache/pip  # Clear cache to free up space
workon $(lsvirtualenv -b | head -n 1) # Activate the first env
pip install --no-cache-dir -r Source\ Code/requirements.txt

# 3. Download Data
echo "[3/4] Downloading NLP Data (NLTK & SpaCy)..."
python Source\ Code/download_nltk.py
python -m spacy download en_core_web_sm

echo "--------------------------------------------------"
echo "    SETUP COMPLETE!                               "
echo "--------------------------------------------------"
echo "Now go to the 'Web' tab and configure your WSGI file."
