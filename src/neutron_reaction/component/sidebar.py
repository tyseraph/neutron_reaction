"""Sidebar component providing navigation links."""


def sidebar():
    """Return the sidebar layout."""
    from dash import html, dcc

    return html.Div(
        [
            html.H2("流程"),
            html.Hr(),
            dcc.Link("首页", href="/", style={"display": "block", "margin": "8px 0"}),
        dcc.Link(
            "核素选择",
            href="/select-nuclide",
            style={"display": "block", "margin": "8px 0"},
        ),
        ],
        style={
            "width": "16rem",
            "padding": "1rem",
            "background": "#f8f9fa",
            "position": "fixed",
            "height": "100vh",
        },
    )
