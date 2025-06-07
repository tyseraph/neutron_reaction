"""Nuclide selection page that combines the chart and NUBASE table."""

import os

try:  # Optional imports so tests pass without dependencies
    import pandas as pd
    from bs4 import BeautifulSoup
except Exception:  # pragma: no cover - used when dependencies missing
    pd = None
    BeautifulSoup = None
from neutron_reaction.data.nuclides import generate_nuclide_data

# Path to the bundled NUBASE HTML table
HTML_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase.html")
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


def _create_figure(selected=None):
    """Return a Plotly N–Z chart.

    Parameters
    ----------
    selected : list[dict] | None
        Nuclide dictionaries to highlight in the chart.
    """
    from plotly import graph_objs as go

    data = generate_nuclide_data()

    scatter = go.Scatter(
        x=[d["N"] for d in data],
        y=[d["Z"] for d in data],
        mode="markers+text",
        text=[d["symbol"] for d in data],
        customdata=data,
        marker=dict(size=18, color="cornflowerblue", symbol="square"),
        textposition="middle center",
        hovertemplate="N=%{x}<br>Z=%{y}<br>%{customdata[symbol]}-%{customdata[A]}<extra></extra>",
    )

    fig = go.Figure(scatter)
    fig.update_layout(
        xaxis_title="N",
        yaxis_title="Z",
        dragmode="select",
        height=600,
    )

    if selected:
        labels = [d["label"] for d in data]
        indices = [
            i
            for i, lbl in enumerate(labels)
            if any(lbl == s.get("label") for s in selected)
        ]
        fig.update_traces(
            selectedpoints=indices,
            selected=dict(marker=dict(color="orange", size=20)),
            unselected=dict(marker=dict(opacity=0.3)),
        )
    return fig


def layout():
    """Return the nuclide selection page layout."""
    from dash import html, dcc, dash_table

    if NUBASE_DF is None:
        table = html.Div("NUBASE 数据表需要 pandas 和 BeautifulSoup 支持")
        dropdown = dcc.Dropdown(options=[], placeholder="未能加载数据", id="nuclide-dropdown")
    else:
        table = dash_table.DataTable(
            id="nuclide-table",
            columns=[{"name": c, "id": c} for c in NUBASE_DF.columns],
            data=NUBASE_DF.to_dict("records"),
            filter_action="native",
            sort_action="native",
            page_size=50,
            style_table={"overflowX": "auto", "maxHeight": "600px", "overflowY": "auto"},
            style_cell={"fontSize": "12px", "textAlign": "center"},
        )
        dropdown = dcc.Dropdown(
            id="nuclide-dropdown",
            options=[{"label": row["Nuclide"], "value": idx} for idx, row in NUBASE_DF.iterrows()],
            placeholder="选择一个核素",
        )

    return html.Div(
        [
            html.H1("核素选择"),
            dcc.Link("查看说明", href="/nubase", style={"marginRight": "1rem"}),
            dcc.Link("返回首页", href="/", style={"marginRight": "1rem"}),
            dcc.Graph(id="nuclide-chart", figure=_create_figure()),
            table,
            dropdown,
            html.Div("请选择一个核素", id="nuclide-selected", style={"fontWeight": "bold", "marginTop": "1rem"}),
            dcc.Store(id="selected-nuclides"),
            html.Div(id="nuclide-output"),
        ]
    )


def register_callbacks(app):
    """Register callbacks for the nuclide selection page."""
    from dash.dependencies import Input, Output, State
    from dash import html

    @app.callback(
        Output("selected-nuclides", "data"),
        Input("nuclide-chart", "selectedData"),
        Input("nuclide-chart", "clickData"),
        State("selected-nuclides", "data"),
    )
    def _store_selection(selected, clicked, current):
        current = current or []
        if selected and "points" in selected:
            current = [p["customdata"] for p in selected["points"]]
        if clicked and "points" in clicked:
            item = clicked["points"][0]["customdata"]
            if item not in current:
                current.append(item)
        return current

    @app.callback(Output("nuclide-output", "children"), Input("selected-nuclides", "data"))
    def _display_selected(data):
        if not data:
            return "未选择核素"
        items = [f"{d['symbol']}-{d['A']} (Z={d['Z']}, N={d['N']})" for d in data]
        return html.Ul([html.Li(item) for item in items])

    @app.callback(Output("nuclide-chart", "figure"), Input("selected-nuclides", "data"))
    def _highlight_selected(data):
        return _create_figure(data)

    @app.callback(
        Output("nuclide-selected", "children"),
        Input("nuclide-dropdown", "value"),
    )
    def _show_dropdown_selection(value):
        if value is not None and NUBASE_DF is not None:
            row = NUBASE_DF.iloc[value]
            return f"已选择：{row.to_dict()}"
        return "请选择一个核素"

