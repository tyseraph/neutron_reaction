# Neutron Reaction

This repository aims to build an interactive nuclear data evaluation platform based on [Dash](https://dash.plotly.com/).

## Features
- Interactive web application with a multi-step workflow
- Separate modules for UI components and pages
- Basic test structure using `pytest`

## Getting Started

1. Install the dependencies (if any).
2. Run the Dash application:
   ```bash
   python -m neutron_reaction.app
   ```

   The application opens with a page titled `核数据智能评价平台` describing the project and linking to the nuclide selection page.

## Directory Structure

- `src/neutron_reaction/`
  - `app.py` – application entry point
  - `layout.py` – top level layout including sidebar and page container
  - `component/` – reusable UI components (e.g., sidebar)
  - `pages/` – individual page layouts such as `home` and `select_nuclide`
- `tests/` – unit tests

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
