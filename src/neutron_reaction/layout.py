"""Application layout that includes the sidebar and page container."""

from .component.sidebar import sidebar


def serve_layout():
    """Return the layout for the Dash application."""
    from dash import html, dcc

    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            sidebar(),
            html.Div(
                id="page-content",
                style={"marginLeft": "18rem", "padding": "2rem"},
            ),
        ]
    )


