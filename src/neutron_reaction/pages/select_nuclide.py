"""Nuclide selection page showing a local NUBASE table."""

import os

try:  # Optional imports so tests pass without dependencies
    import pandas as pd
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - used when dependencies missing
    pd = None
    BeautifulSoup = None

# Path to the bundled NUBASE HTML table
HTML_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase_min.html")
)


from typing import Any


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
    from dash import html, dcc

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        src_doc = f.read()

    if NUBASE_DF is None:
        dropdown = dcc.Dropdown(
            options=[],
            placeholder="NUBASE 数据表需要 pandas 和 BeautifulSoup 支持",
            id="nuclide-dropdown",
            multi=True,
        )
    else:
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
            html.H1("核素选择"),
            dcc.Link("返回首页", href="/", style={"marginRight": "1rem"}),
            html.Iframe(
                srcDoc=src_doc,
                style={"width": "100%", "height": "800px", "border": "none"},
            ),
            dropdown,
            html.Div(
                "请选择一个核素",
                id="nuclide-selected",
                style={"fontWeight": "bold", "marginTop": "1rem"},
            ),
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
        if value and NUBASE_DF is not None:
            # When multi=True, value may be a list
            if not isinstance(value, list):
                value = [value]
            rows = [NUBASE_DF.iloc[v] for v in value]
            labels = [f"{i}-{row['Nuclide']}" for i, row in zip(value, rows)]
            return "已选择：" + ", ".join(labels)
        return "请选择一个核素"

