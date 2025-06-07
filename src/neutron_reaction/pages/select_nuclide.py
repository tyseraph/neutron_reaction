"""Nuclide selection page embedding the NUBASE table."""

from pathlib import Path

try:  # Optional imports so tests pass without dependencies
    import pandas as pd
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - used when dependencies missing
    pd = None
    BeautifulSoup = None

# Path to the bundled NUBASE HTML table
HTML_PATH = Path(__file__).resolve().parent.parent / "data" / "nubase.html"


from typing import Any

# Dropdown fallback when NUBASE cannot be parsed
MANUAL_OPTIONS = [
    {"label": "H-1", "value": "H-1"},
    {"label": "He-4", "value": "He-4"},
    {"label": "Na-23", "value": "Na-23"},
]


def parse_nubase_html(html_file: str) -> Any:
    """Parse the local NUBASE HTML and return it as a DataFrame.

    Raises
    ------
    ImportError
        If pandas or BeautifulSoup are not available.
    """
    if pd is None or BeautifulSoup is None:
        raise ImportError("pandas and BeautifulSoup are required to parse NUBASE")

    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    table = soup.find("table")
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) == len(headers):
            rows.append(cells)
    return pd.DataFrame(rows, columns=headers)


try:  # May fail if dependencies are missing
    NUBASE_DF = parse_nubase_html(HTML_PATH)
except Exception:  # pragma: no cover - handled gracefully during tests
    NUBASE_DF = None


def layout():
    """Return the nuclide selection page layout."""
    from dash import html, dcc, dash_table

    if NUBASE_DF is None:
        table = html.P("缺少 pandas 或 BeautifulSoup，无法加载 NUBASE 表")
        dropdown = dcc.Dropdown(
            id="nuclide-dropdown",
            options=MANUAL_OPTIONS,
            placeholder="NUBASE 表不可用，选择示例核素",
            multi=True,
        )
    else:
        table = dash_table.DataTable(
            id="nuclide-table",
            columns=[{"name": c, "id": c} for c in NUBASE_DF.columns],
            data=NUBASE_DF.to_dict("records"),
            filter_action="native",
            sort_action="native",
            page_size=100,
            row_selectable="single",
            style_table={"overflowX": "auto", "maxHeight": "800px", "overflowY": "auto"},
            style_cell={"fontSize": "12px", "textAlign": "center", "maxWidth": "200px"},
        )
        dropdown = dcc.Dropdown(
            id="nuclide-dropdown",
            options=[
                {"label": f"{idx}-{row['Nuclide']}", "value": idx}
                for idx, row in NUBASE_DF.iterrows()
            ],
            placeholder="选择核素，可多选",
            multi=True,
        )

    return html.Div(
        [
            html.H3("核素选取"),
            table,
            dropdown,
            html.Br(),
            html.Div("请选择一个核素", id="nuclide-selected", style={"fontWeight": "bold"}),
        ]
    )


def register_callbacks(app):
    """Register callbacks for the nuclide selection page."""
    from dash.dependencies import Input, Output

    @app.callback(
        Output("nuclide-selected", "children"),
        Input("nuclide-dropdown", "value"),
    )
    def _show_dropdown_selection(value):
        if not value:
            return "请选择一个核素"

        if NUBASE_DF is not None:
            if not isinstance(value, list):
                value = [value]
            rows = [NUBASE_DF.iloc[v] for v in value]
            labels = [f"{i}-{row['Nuclide']}" for i, row in zip(value, rows)]
            return "已选择：" + ", ".join(labels)

        # Fallback when NUBASE table is unavailable
        if not isinstance(value, list):
            value = [value]
        return "已选择：" + ", ".join(value)

