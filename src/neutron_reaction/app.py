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

    index_page = html.Div(
        [
            html.H1(
                "欢迎使用核数据智能评价平台",
                style={"textAlign": "center"},
            ),
            html.Hr(),
            html.Div(
                [
                    dcc.Link("平台简介", href="/intro", style={"margin": "0 10px"}),
                    dcc.Link("功能流程图", href="/workflow", style={"margin": "0 10px"}),
                    dcc.Link("快速上手视频", href="/video", style={"margin": "0 10px"}),
                ],
                style={"textAlign": "center"},
            ),
            html.Br(),
            html.Div(
                [
                    dcc.Link(
                        "立即开始新任务",
                        href="/nuclide",
                        style={"display": "block", "margin": "10px"},
                    ),
                    dcc.Link(
                        "继续上次任务",
                        href="/resume",
                        style={"margin": "10px"},
                    ),
                    dcc.Link(
                        "浏览案例流程",
                        href="/cases",
                        style={"margin": "10px"},
                    ),
                ],
                style={"textAlign": "center"},
            ),
        ]
    )

    nuclide_page = html.Div([
        html.H1("核素选择"),
        dcc.Link("下一步: 模型选择", href="/model"),
    ])

    intro_page = html.Div([
        html.H1("平台简介"),
        dcc.Link("返回首页", href="/"),
    ])

    workflow_page = html.Div([
        html.H1("功能流程图"),
        dcc.Link("返回首页", href="/"),
    ])

    video_page = html.Div([
        html.H1("快速上手视频"),
        dcc.Link("返回首页", href="/"),
    ])

    resume_page = html.Div([
        html.H1("继续上次任务"),
        dcc.Link("下一步: 核素选择", href="/nuclide"),
    ])

    cases_page = html.Div([
        html.H1("浏览案例流程"),
        dcc.Link("返回首页", href="/"),
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
        if pathname == "/intro":
            return intro_page
        if pathname == "/workflow":
            return workflow_page
        if pathname == "/video":
            return video_page
        if pathname == "/resume":
            return resume_page
        if pathname == "/cases":
            return cases_page
        return index_page

    return app


if __name__ == "__main__":
    app = create_dash_app()
    app.run_server(debug=True)
