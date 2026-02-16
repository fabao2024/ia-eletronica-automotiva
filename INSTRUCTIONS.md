# Local Run Instructions

Use this guide to run the Streamlit MVP locally and validate the core prototype flows.

## Prerequisites

- Python 3.8 or newer
- Pip
- Git (optional, if cloning the repository)

## Quick Start

```bash
git clone https://github.com/fabao2024/ia-eletronica-automotiva.git
cd ia-eletronica-automotiva

python -m venv .venv
# Windows
.\\.venv\\Scripts\\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Open `http://127.0.0.1:8501` (or `http://localhost:8501`).

## What to Validate

- App starts without exceptions.
- All tabs render correctly.
- Images in `mockups/` load.
- Upload workflow works with a sample image.
- Camera workflow stays disabled until user explicitly enables it.

## VS Code / Cursor

1. Open the repository folder.
2. Select the Python interpreter from `.venv`.
3. Run the `Python: Streamlit` launch profile (`F5`).

## Troubleshooting

- `ERR_CONNECTION_REFUSED`
: Make sure Streamlit is still running in the terminal.
- `streamlit: command not found`
: Activate `.venv` first, then rerun.
- Font issues in image generation
: Install common system fonts or use the default fallback in `app.py`.
- Camera prompt appears unexpectedly
: Clear browser permission cache for localhost and reload.
