# Hesabu+

Hesabu+ uses a React frontend with a FastAPI backend.

## Current Layout

```text
frontend/
	index.html
	package.json
	vite.config.js
	src/
		App.jsx
		main.jsx
		styles.css
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

- The frontend is built with React and Vite.
- `backend/app/main.py` serves the React build when available and exposes the API.
- Calculation preview logic lives under `backend/app/modules/`.

## Run Locally

1. Install backend dependencies with `pip install -r backend/requirements.txt`.
2. Install frontend dependencies with `cd frontend && npm install`.
3. Start the backend with `uvicorn backend.app.main:app --reload`.
4. Start the React dev server with `cd frontend && npm run dev`.
