"""NUBASE reference page."""

NUBASE_URL = "https://www-nds.iaea.org/relnsd/nubase/nubase_min.html"


def layout():
    """Return the layout for the NUBASE information page."""
    from dash import html
    return html.Div(
        [
            html.H1("NUBASE 数据表"),
            html.P(
                [
                    "该页面链接至 IAEA 发布的 ",
                    html.A("NUBASE", href=NUBASE_URL, target="_blank"),
                    " 表，可作为核素选择与参考。",
                ]
            ),
            html.Ul(
                [
                    html.Li("点击上方链接在新标签页打开 NUBASE 表"),
                    html.Li("在左侧导航返回其他页面"),
                ]
            ),
        ]
    )
