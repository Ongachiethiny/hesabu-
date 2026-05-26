from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import importlib
from pathlib import Path
import sys


def _import_db_and_models():
    """Try several import strategies so this module works when run as a script
    (`python backend/app/main.py`) or imported as a package by a WSGI/ASGI server.
    """
    try:
        # Preferred when imported as a package (e.g., uvicorn backend.app.main:app)
        from .database import SessionLocal, engine, Base  # type: ignore
        from . import models  # noqa: F401
        return SessionLocal, engine, Base
    except Exception:
        # Try importing using the package name (requires `backend` to be on sys.path)
        try:
            db = importlib.import_module("backend.app.database")
            importlib.import_module("backend.app.models")
            return db.SessionLocal, db.engine, db.Base
        except Exception:
            # As a last resort, try to import by file path (less reliable for relative imports)
            base_dir = Path(__file__).resolve().parent
            sys.path.insert(0, str(base_dir))
            try:
                db = importlib.import_module("database")
                importlib.import_module("models")
                return db.SessionLocal, db.engine, db.Base
            finally:
                if str(base_dir) in sys.path:
                    sys.path.remove(str(base_dir))


SessionLocal, engine, Base = _import_db_and_models()

# 1. Automatically create database tables when the app starts
Base.metadata.create_all(bind=engine)

app = FastAPI(title="HesabuEngine API", version="1.0")

# 2. Database Dependency (The "Gatekeeper")
# This opens a database session for a single request, and closes it automatically
# when the request is done. This prevents memory leaks.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 3. Test Route 1: A simple welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to HesabuEngine API! Backend is running smoothly."}


# 4. Test Route 2: Create a dummy project directly in the DB
@app.post("/test-create-project/")
def create_test_project(name: str, description: str, db: Session = Depends(get_db)):
    # Create an instance of the Project model (We hardcode user_id=1 for testing)
    new_project = models.Project(
        name=name,
        description=description,
        user_id=1 
    )
    
    # Stage and save it to 'hesabu.db'
    db.add(new_project)
    db.commit()
    db.refresh(new_project) # Refreshes to get the auto-generated ID from SQLite
    
    return {"status": "Success", "project": new_project}


# 5. Test Route 3: Fetch all saved projects from the DB
@app.get("/test-get-projects/")
def get_test_projects(db: Session = Depends(get_db)):
    projects = db.query(models.Project).all()
    return {"projects": projects}