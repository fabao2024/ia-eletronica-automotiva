# Automotive Electronics AI

This repository is an MVP for an AI-assisted automotive electronics platform.
The current focus is an interactive Streamlit prototype that demonstrates guided diagnostics and visual-analysis workflows.

## Overview

- Guided AI diagnostic flow
- Visual interpretation workflow for components and schematics
- Knowledge-base style output and dashboard mockups
- Architecture ready for future backend and model integrations

## Current Repository Scope

- This repository currently delivers a visual MVP (interactive mockups).
- Runtime stack in code: `Python`, `Streamlit`, and `Pillow`.
- Mockup PNG files in `mockups/` are generated only when missing.
- Camera capture is opt-in and requires explicit user action in the UI.

## Run Locally

### Prerequisites

- Python 3.8+
- Pip
- VS Code (optional)

### Setup

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

### VS Code / Cursor Run

1. Open the project folder.
2. Select the `.venv` interpreter.
3. Use the `Python: Streamlit` launch profile in Run and Debug (`F5`).

## Documentation

- `INSTRUCTIONS.md`: step-by-step local execution and troubleshooting
- `AGENTS.md`: contributor and workflow guidelines

## Planned Next Steps

- Add real backend/API integration
- Add production data pipeline for diagnostics
- Integrate computer vision and NLP model components
- Release beta version for partner workshops

## Contributing

Contributions are welcome. Open an issue or pull request with a clear summary and test evidence.

## License

This project is licensed under MIT.
