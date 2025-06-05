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
            html.Div("[平台LOGO]", style={"textAlign": "center", "fontSize": "24px"}),
            html.H1(
                "核数据智能评价平台",
                style={"textAlign": "center"},
            ),
            html.Hr(),
            html.P(
                "本平台旨在为核数据评价与理论建模提供高效、可视化、智能化的分析工具，支持多模型、多反应道实验数据的比对与拟合，适合科研与专业评价",
                style={"textAlign": "center"},
            ),
            html.Ul(
                [
                    html.Li("批量核素与反应道的可视化对比和数据管理"),
                    html.Li("主流理论模型的一键拟合与参数优化"),
                    html.Li("实验与评价数据自动筛选、目标数据定制"),
                    html.Li("多类型输出与报告生成"),
                ]
            ),
            html.Div(
                [
                    dcc.Link("进入核素选择", href="/nuclide", style={"margin": "0 10px"}),
                    dcc.Link("功能说明/帮助", href="/help", style={"margin": "0 10px"}),
                    dcc.Link("文档", href="/docs", style={"margin": "0 10px"}),
                ],
                style={"textAlign": "center"},
            ),
            html.Br(),
            html.Div(
                [
                    dcc.Link("团队/项目介绍", href="/team", style={"margin": "0 10px"}),
                    dcc.Link("联系邮箱", href="mailto:contact@example.com", style={"margin": "0 10px"}),
                    dcc.Link("版本信息", href="/version", style={"margin": "0 10px"}),
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

    help_page = html.Div([
        html.H1("功能说明/帮助"),
        dcc.Link("返回首页", href="/"),
    ])

    docs_page = html.Div([
        html.H1("文档"),
        dcc.Link("返回首页", href="/"),
    ])

    team_page = html.Div([
        html.H1("团队/项目介绍"),
        dcc.Link("返回首页", href="/"),
    ])

    version_page = html.Div([
        html.H1("版本信息"),
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
        if pathname == "/help":
            return help_page
        if pathname == "/docs":
            return docs_page
        if pathname == "/team":
            return team_page
        if pathname == "/version":
            return version_page
        return index_page

    return app


if __name__ == "__main__":
    app = create_dash_app()
    app.run_server(debug=True)
