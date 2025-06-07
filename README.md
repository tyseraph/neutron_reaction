# Neutron Reaction

This repository aims to build an interactive nuclear data evaluation platform based on [Dash](https://dash.plotly.com/).

## Features
- Interactive web application with a multi-step workflow
- Separate modules for UI components and pages
- Basic test structure using `pytest`
- Nuclide selection page embeds the local `nubase.html` table (stored in
  `src/neutron_reaction/data/nubase.html`) inside an interactive grid.
  Select a row directly from this table to choose a nuclide for study.

## Getting Started

1. Install the dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Dash application from the project root so that imports resolve correctly:
```bash
python -m neutron_reaction.app
```

The application opens with a page titled `核数据智能评价平台` describing the project and linking to the nuclide selection page. On that page the local NUBASE table is shown in a `dash_table.DataTable` where you can filter, sort and select a row to pick a nuclide. All modules now use absolute imports (e.g. `from neutron_reaction.layout import serve_layout`) to avoid issues when the application is executed directly or as a module.

## Directory Structure

- `src/neutron_reaction/`
  - `app.py` – application entry point
  - `layout.py` – top level layout including sidebar and page container
  - `component/` – reusable UI components (e.g., sidebar)
  - `pages/` – individual page layouts such as `home` and `select_nuclide`
- `tests/` – unit tests

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
