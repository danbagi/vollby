# voll.by — Slovak Election Polling Dashboard

## Requirements

- Python 3.11+

## Installation

```bash
cd backend
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload --port 8000
```

API docs available at: http://localhost:8000/docs

## Frontend

Open the HTML files in a browser, or serve locally:

```bash
cd frontend
python -m http.server 3000
```

Then open http://localhost:3000/vollby.html

## Quick start (backend + venv)

```bash
./start.sh
```
