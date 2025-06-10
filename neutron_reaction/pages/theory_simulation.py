from dash import html

def layout():
    return html.Div([
        html.H3("理论模拟页面"),
        html.P("此处可放理论模型拟合/参数联动/绘图等功能。"),
        html.Button("进入成果展示与数据保存", id="goto-results", n_clicks=0, style={"marginTop": "2rem"}),
    ])
