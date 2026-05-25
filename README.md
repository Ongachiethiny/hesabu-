# Hesabu+

Hesabu+ is currently organized as a backend-first project.

## Current Layout

```text
frontend/
	index.html
	styles.css
	app.js
backend/
	app/
		__init__.py
		main.py
		database.py
		models.py
		schemas.py
		modules/
			__init__.py
			mechanical.py
			structural.py
			electrical.py
	requirements.txt
```

## Notes

- The frontend is a static single-page app for now.
- `backend/app/main.py` serves the frontend and API.
- Calculation preview logic lives under `backend/app/modules/`.

## Run Locally

1. Install backend dependencies with `pip install -r backend/requirements.txt`.
2. Start the app with `uvicorn backend.app.main:app --reload`.
3. Open `http://127.0.0.1:8000/` in your browser.
