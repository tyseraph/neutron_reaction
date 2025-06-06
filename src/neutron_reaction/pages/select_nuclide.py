"""Nuclide selection page with an interactive nuclide chart."""

from neutron_reaction.data.nuclides import generate_nuclide_data


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
        mode="markers",
        text=[d["label"] for d in data],
        customdata=data,
        marker=dict(size=6, color="#1f77b4"),
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
            selected=dict(marker=dict(color="red", size=8)),
            unselected=dict(marker=dict(opacity=0.3)),
        )
    return fig


def layout():
    """Return the nuclide selection page layout."""
    from dash import html, dcc

    return html.Div(
        [
            html.H1("核素选择"),
            dcc.Link("返回首页", href="/", style={"marginRight": "1rem"}),
            dcc.Graph(id="nuclide-chart", figure=_create_figure()),
            dcc.Store(id="selected-nuclides"),
            html.Div(id="nuclide-output"),
        ]
    )


def register_callbacks(app):
    """Register callbacks for the nuclide selection page."""
    from dash.dependencies import Input, Output
    from dash import html

    @app.callback(
        Output("selected-nuclides", "data"), Input("nuclide-chart", "selectedData")
    )
    def _store_selection(selected):
        if selected and "points" in selected:
            return [p["customdata"] for p in selected["points"]]
        return []

    @app.callback(Output("nuclide-output", "children"), Input("selected-nuclides", "data"))
    def _display_selected(data):
        if not data:
            return "未选择核素"
        items = [f"{d['symbol']}-{d['A']} (Z={d['Z']}, N={d['N']})" for d in data]
        return html.Ul([html.Li(item) for item in items])

    @app.callback(Output("nuclide-chart", "figure"), Input("selected-nuclides", "data"))
    def _highlight_selected(data):
        return _create_figure(data)

