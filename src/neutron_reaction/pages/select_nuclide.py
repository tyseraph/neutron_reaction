"""Nuclide selection page."""


def layout():
    """Return the nuclide selection page layout."""
    from dash import html, dcc

    return html.Div([
        html.H1("核素选择"),
        dcc.Link("返回首页", href="/", style={"marginRight": "1rem"}),
    ])

