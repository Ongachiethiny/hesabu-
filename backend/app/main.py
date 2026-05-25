from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .modules.electrical import preview_electrical
from .modules.mechanical import preview_mechanical
from .modules.structural import preview_structural
from .schemas import ElectricalPreviewRequest, MechanicalPreviewRequest, StructuralPreviewRequest


BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(title="Hesabu+ API")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

if FRONTEND_DIR.exists():
	app.mount("/frontend", StaticFiles(directory=str(FRONTEND_DIR)), name="frontend")


@app.get("/")
def index() -> FileResponse:
	index_path = FRONTEND_DIR / "index.html"
	if not index_path.exists():
		raise HTTPException(status_code=404, detail="Frontend is not available")
	return FileResponse(index_path)


@app.get("/api/health")
def health() -> dict[str, str]:
	return {"status": "ok"}


@app.post("/api/calculators/mechanical/preview")
def mechanical_preview(payload: MechanicalPreviewRequest) -> dict[str, object]:
	return preview_mechanical(payload)


@app.post("/api/calculators/structural/preview")
def structural_preview(payload: StructuralPreviewRequest) -> dict[str, object]:
	return preview_structural(payload)


@app.post("/api/calculators/electrical/preview")
def electrical_preview(payload: ElectricalPreviewRequest) -> dict[str, object]:
	return preview_electrical(payload)
