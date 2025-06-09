"""Nuclide selection page displaying the local NUBASE table."""

from __future__ import annotations

import os

try:  # Optional imports so tests pass if dependencies are missing
    import pandas as pd
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - handled when packages absent
    pd = None
    BeautifulSoup = None

# Path to the bundled NUBASE HTML file
HTML_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase.html")
)
def parse_nubase_html(html_file: str) -> "pd.DataFrame":
    """Parse the local NUBASE HTML table into a DataFrame."""
    if pd is None or BeautifulSoup is None:
        raise ImportError("pandas and BeautifulSoup are required to parse NUBASE")
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    table = soup.find("table")
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr")[1:]:  # skip header row
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) == len(headers):
            rows.append(cells)

    return pd.DataFrame(rows, columns=headers)
def _load_dataframe() -> "pd.DataFrame | None":
    try:
        return parse_nubase_html(HTML_PATH)
    except Exception:  # pragma: no cover - show message instead
        return None
    if NUCLIDE_DF is None:
            html.P("无法加载 NUBASE 表，请安装 pandas 和 beautifulsoup4"),
        columns=[{"name": c, "id": c} for c in NUCLIDE_DF.columns],
        data=NUCLIDE_DF.to_dict("records"),
        page_size=100,
    return html.Div([
        html.H3("核素选取"),
        table,
        html.Br(),
        html.Div("请选择一个核素", id="nuclide-selected", style={"fontWeight": "bold"}),
    ])
    """Register callbacks for this page."""
    @app.callback(Output("nuclide-selected", "children"), Input("nuclide-table", "selected_rows"))
    def _show_selected_nuclide(selected_rows):
            return f"已选择：{row.to_dict()}"
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
