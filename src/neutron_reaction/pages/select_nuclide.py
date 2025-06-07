"""Nuclide selection page embedding the NUBASE table."""

from pathlib import Path

try:  # Optional imports so tests pass without dependencies
    import pandas as pd
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - used when dependencies missing
    pd = None
    BeautifulSoup = None

# Path to the bundled NUBASE HTML table
    from dash import html, dash_table
        return html.Div([
            html.H3("核素选取"),
            html.P("缺少 pandas 或 BeautifulSoup，无法加载 NUBASE 表"),
        ])

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
    if NUBASE_DF is None:
        return

        Input("nuclide-table", "selected_rows"),
    def _show_selected_row(selected_rows):
        if selected_rows:
            row = NUBASE_DF.iloc[selected_rows[0]]
            return f"已选择：{row.to_dict()}"
        return "请选择一个核素"
            options=[],
            placeholder="NUBASE 数据表需要 pandas 和 BeautifulSoup 支持",
            id="nuclide-dropdown",
            multi=True,
        )
    else:
        dropdown = dcc.Dropdown(
            id="nuclide-dropdown",
            options=[
                {"label": f"{row['Nuclide']}", "value": idx}
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
