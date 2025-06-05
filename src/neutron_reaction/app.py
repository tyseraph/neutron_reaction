"""Dash application for the nuclear data evaluation platform."""


def interactive_message() -> str:
    """Return a welcome message for the interactive platform."""
    return "Welcome to the Nuclear Data Evaluation Platform"


def create_dash_app():
    """Create and return the Dash application."""
    import dash
    from dash import dcc, html
    from dash.dependencies import Input, Output

    app = dash.Dash(__name__, suppress_callback_exceptions=True)

    index_page = html.Div([
        html.H1("首页/入门"),
        dcc.Link("下一步: 核素选择", href="/nuclide"),
    ])

    nuclide_page = html.Div([
        html.H1("核素选择"),
        dcc.Link("下一步: 模型选择", href="/model"),
    ])

    model_page = html.Div([
        html.H1("模型选择"),
        dcc.Link("下一步: 反应道选择", href="/reaction"),
    ])

    reaction_page = html.Div([
        html.H1("反应道选择"),
        dcc.Link("下一步: 实验数据筛选", href="/experiment"),
    ])

    experiment_page = html.Div([
        html.H1("实验数据筛选"),
        dcc.Link("下一步: 目标数据确认", href="/target"),
    ])

    target_page = html.Div([
        html.H1("目标数据确认"),
        dcc.Link("下一步: 理论模型拟合与可视化", href="/fit"),
    ])

    fit_page = html.Div([
        html.H1("理论模型拟合与可视化"),
        dcc.Link("下一步: 结果与报告导出", href="/result"),
    ])

    result_page = html.Div([
        html.H1("结果与报告导出"),
        dcc.Link("回到首页", href="/"),
    ])

    app.layout = html.Div([
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ])

    @app.callback(Output("page-content", "children"), Input("url", "pathname"))
    def display_page(pathname):
        if pathname == "/nuclide":
            return nuclide_page
        if pathname == "/model":
            return model_page
        if pathname == "/reaction":
            return reaction_page
        if pathname == "/experiment":
            return experiment_page
        if pathname == "/target":
            return target_page
        if pathname == "/fit":
            return fit_page
        if pathname == "/result":
            return result_page
        return index_page

    return app


if __name__ == "__main__":
    app = create_dash_app()
    app.run_server(debug=True)
