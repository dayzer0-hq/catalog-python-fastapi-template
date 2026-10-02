# DayZer0 — Python + FastAPI starter

A minimal, runnable FastAPI service. It ships with one route — a health check
at `GET /healthz` — and nothing else. Your project's tickets build the real
endpoints on top of this skeleton; you do not need to create the app, pick the
framework, or wire up a health check.

## Stack

- Python 3.11+
- [FastAPI](https://fastapi.tiangolo.com/) for the app and request/response models
- [uvicorn](https://www.uvicorn.org/) as the ASGI server
- [pytest](https://docs.pytest.org/) for tests

## Run it

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/healthz — it answers `{"status": "ok"}`.

## Test it

```bash
pytest
```

## Layout

```
app/
  main.py        the FastAPI app and the /healthz route — add your routes here
tests/
  test_health.py a test for the health check — add your tests alongside it
requirements.txt pinned dependencies
```
