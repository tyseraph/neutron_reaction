"""Local NUBASE reference page."""

import os

HTML_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase.html")
)


def layout():
    """Return the layout for the NUBASE information page."""
    from dash import html

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        src_doc = f.read()

    return html.Div(
        [
            html.H1("NUBASE 数据表"),
            html.P("下面展示的是本地存储的 NUBASE 表，可供参考。"),
            html.Iframe(
                srcDoc=src_doc,
                style={"width": "100%", "height": "800px", "border": "none"},
            ),
        ]
    )
