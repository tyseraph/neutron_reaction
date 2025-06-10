from dash import html

def layout():
    return html.Div([
        html.H3("成果展示与数据保存页面"),
        html.P("展示所有计算结果、导出数据和保存功能。"),
        html.Button("返回理论模拟", id="back-to-simulation", n_clicks=0, style={"marginTop": "2rem"}),
    ])
