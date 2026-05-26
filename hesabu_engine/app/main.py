from fastapi import FastAPI

from .routers import machine_design, thermodynamics, fluid_mechanics
from .database import init_db


app = FastAPI(title="hesabu_engine")


@app.on_event("startup")
def on_startup():
    # Ensure database and any startup tasks run
    init_db()


app.include_router(machine_design.router, prefix="/api/machine_design", tags=["machine_design"])
app.include_router(thermodynamics.router, prefix="/api/thermodynamics", tags=["thermodynamics"])
app.include_router(fluid_mechanics.router, prefix="/api/fluid_mechanics", tags=["fluid_mechanics"])


@app.get("/api/health")
def health():
    return {"status": "ok"}
