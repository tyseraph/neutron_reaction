# Neutron Reaction

This repository aims to build an interactive nuclear data evaluation platform based on [Dash](https://dash.plotly.com/).

## Features
- Interactive web application with a multi-step workflow
- Separate modules for UI components and pages
- Basic test structure using `pytest`
- Home page links to the online [NUBASE](https://www-nds.iaea.org/nubase/) table
  so you can look up properties for each nuclide.
- The nuclide selection page parses the bundled `nubase.html` table so you can
  choose a nuclide directly from the data. The table is displayed in a
  `dash_table.DataTable` where a row can be selected.

## Getting Started

1. Install the dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
   The nuclide table also requires `pandas` and `beautifulsoup4`:
   ```bash
   pip install pandas beautifulsoup4
   ```
2. Run the Dash application from the project root so that imports resolve correctly:
```bash
python -m neutron_reaction.app
```

The application opens with a page titled `核数据智能评价平台` describing the project and linking to the nuclide selection page. The home page also provides a link to the official NUBASE database for browsing nuclide properties. On the selection page the data are loaded from the bundled `nubase.html` file and presented in a `dash_table.DataTable` where you can pick one nuclide. All modules use absolute imports (e.g. `from neutron_reaction.layout import serve_layout`) to avoid issues when the application is executed directly or as a module.

## Directory Structure

- `src/neutron_reaction/`
  - `app.py` – application entry point
  - `layout.py` – top level layout including sidebar and page container
  - `component/` – reusable UI components (e.g., sidebar)
  - `pages/` – individual page layouts such as `home` and `select_nuclide`
- `tests/` – unit tests

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
