# Cliff-Project

A small Flask app that checks whether a raise would push a household across common Louisiana SNAP and Medicaid income cliffs.

## Run locally

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python cliff_project/app.py
   ```
4. Open the app in your browser:
   ```text
   http://127.0.0.1:5000/
   ```

## Notes

- The app uses Flask and stores the page template in the `cliff_project/templates` folder.
- Static assets like CSS are served from `cliff_project/static` so they load correctly when the project is opened in a browser.
