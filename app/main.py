"""DayZer0 FastAPI starter — a minimal, runnable skeleton.

Build your project's endpoints on top of this. The health check below is the
one route the skeleton ships with; leave it in place and add your own routes
alongside it.
"""

from fastapi import FastAPI

app = FastAPI(title="DayZer0 FastAPI starter")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    """Liveness probe. Returns 200 with a small JSON body."""
    return {"status": "ok"}
