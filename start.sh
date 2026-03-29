#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/backend"

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Starting server at http://localhost:8000"
uvicorn main:app --reload --port 8000
