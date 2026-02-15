# Repository Guidelines

## Project Structure & Module Organization
- Core application lives in `app.py` (single Streamlit entry point).
- Generated and reference UI images live in `mockups/` (`login.png`, `dashboard.png`, etc.).
- Documentation is in `README.md` and `INSTRUCOES.md`.
- Environment/editor setup is in `.devcontainer/devcontainer.json` and `.vscode/launch.json`.
- Dependencies are pinned minimally in `requirements.txt` (`streamlit`, `pillow`).

## Build, Test, and Development Commands
- Create environment: `python -m venv venv`
- Activate (Windows): `.\venv\Scripts\activate`
- Install deps: `pip install -r requirements.txt`
- Run app locally: `streamlit run app.py`
- VS Code debug profile: use `Python: Streamlit` from `.vscode/launch.json`.
- Container workflow (optional): `.devcontainer/devcontainer.json` starts Streamlit on port `8501`.

## Coding Style & Naming Conventions
- Follow Python style: 4-space indentation, `snake_case` for functions/variables, constants in `UPPER_SNAKE_CASE`.
- Keep UI text and labels consistent with the current Portuguese product language.
- Prefer small helper functions (as in `create_mockup`, `save_mockup`) over long inline blocks.
- Use descriptive image names in `mockups/` (example: `vehicle_selection.png`).

## Testing Guidelines
- No automated test suite is configured yet.
- Minimum validation before PR:
  - `python -m py_compile app.py` (syntax check)
  - `streamlit run app.py` and verify all tabs render and images load from `mockups/`.
- If adding logic beyond UI rendering, introduce `pytest` tests under `tests/` and mirror module names (example: `tests/test_mockup_generation.py`).

## Commit & Pull Request Guidelines
- Existing history uses prefixes like `docs:` and `feat:`; continue with Conventional Commit style (`feat:`, `fix:`, `docs:`, `chore:`).
- Keep commit scope focused (UI text, mockup generation, docs, etc.).
- PRs should include:
  - concise summary of behavior changes,
  - manual test evidence (commands run + results),
  - screenshots/GIFs for UI updates,
  - linked issue when applicable.

## Security & Configuration Tips
- Do not commit API keys or tokens.
- If external AI/database integrations are added, load secrets from environment variables (for example, `.env`, excluded from git).
- Avoid adding large binary files unless they are required for demos or documentation.
