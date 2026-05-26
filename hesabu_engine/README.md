hesabu_engine
===============

Small backend package for engineering calculations.

Structure
---------

app/
  - __init__.py
  - main.py (FastAPI app entry)
  - config.py (settings)
  - database.py (SQLAlchemy engine + Base)
  - models.py (User, SavedCalc)
  - core/ (constants, unit_converter)
  - routers/ (machine_design, thermodynamics, fluid_mechanics)

tests/ (pytest unit tests)

Quick start (local dev)

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate on Windows
pip install -r hesabu_engine/requirements.txt
```

2. Run the app:

```bash
uvicorn hesabu_engine.app.main:app --reload
```

3. Health check: GET http://127.0.0.1:8000/api/health
