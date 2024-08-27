#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"

# Start the Flask application
gunicorn app:app
