from dash import html, dcc

def sidebar():
    return html.Div(
        [
            html.H2("核数据平台", style={"textAlign": "center"}),
            html.Hr(),
            dcc.Link("首页", href="/", style={"display": "block", "padding": "1rem"}),
            dcc.Link("核素选取", href="/select-nuclide", style={"display": "block", "padding": "1rem"}),
            dcc.Link("参数选择", href="/model-params", style={"display": "block", "padding": "1rem"}),
            dcc.Link("数据评价", href="/data-evaluation", style={"display": "block", "padding": "1rem"}),
            dcc.Link("理论模拟", href="/theory-simulation", style={"display": "block", "padding": "1rem"}),
            dcc.Link("成果展示", href="/results", style={"display": "block", "padding": "1rem"}),
        ],
        style={
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "18rem",
            "background": "#F8F9FA",
            "padding": "2rem 1rem",
            "boxShadow": "2px 0 5px rgba(0,0,0,0.05)",
            "zIndex": 10,
        }
    )
