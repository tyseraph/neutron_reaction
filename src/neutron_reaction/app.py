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
        style={"maxWidth": "820px", "margin": "auto", "padding": "32px"},
        children=[
            html.Div(
                [
                    html.H1("核数据智能评价平台", style={"marginBottom": "0.2em"}),
                    html.Hr(style={"marginBottom": "1em"}),
                ]
            ),
            html.Div(
                [
                    html.P(
                        "本平台为核数据评价与理论建模的专业用户，提供高效的多模型、多反应道实验数据比对与理论拟合工具。"
                        "支持大批量核素管理、目标数据处理、参数优化与可视化分析，"
                        "适用于核反应数据评价、模型开发与科研分析等场景。"
                    )
                ],
                style={"fontSize": "1.1em", "color": "#333", "marginBottom": "1.2em"},
            ),
            html.Div(
                [
                    html.H3("主要功能", style={"fontSize": "1.16em", "marginBottom": "0.4em"}),
                    html.Ul(
                        [
                            html.Li("多模型、多反应道实验与理论数据可视化对比"),
                            html.Li("实验数据筛选、目标数据处理与误差分析"),
                            html.Li("一键理论模型参数优化与协方差输出"),
                            html.Li("支持批量核素处理和结果报告导出"),
                        ],
                        style={"fontSize": "1em", "marginLeft": "1.3em"},
                    ),
                ],
                style={"marginBottom": "1.2em"},
            ),
            html.Div(
                [
                    dcc.Link(
                        html.Button("进入核素选择", style={"padding": "12px 36px", "fontSize": "1.05em"}),
                        href="/nuclide",
                    ),
                    dcc.Link(
                        html.Button(
                            "功能说明",
                            style={"marginLeft": "18px", "padding": "12px 32px", "fontSize": "1.01em"},
                        ),
                        href="/help",
                    ),
                ],
                style={"marginBottom": "2em", "marginTop": "0.5em"},
            ),
            html.Div(
                [
                    html.P(
                        "技术支持：XXX团队 | 联系方式：contact@xxxx.org",
                        style={"fontSize": "0.98em", "color": "#777"},
                    ),
                    html.P(
                        "版本 v1.0.0 | 引用本平台请注明出处",
                        style={"fontSize": "0.98em", "color": "#bbb"},
                    ),
                ],
                style={"marginTop": "2.5em"},
            ),
        ],
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
