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
- `backend/app/main.py` is the application entry point.
- Calculation logic is intended to live under `backend/app/modules/`.
