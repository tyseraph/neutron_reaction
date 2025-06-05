"""Home page layout."""


def layout():
    """Return the home page layout."""
    from dash import html, dcc

    return html.Div(
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
                    html.H3(
                        "主要功能",
                        style={"fontSize": "1.16em", "marginBottom": "0.4em"},
                    ),
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
                        html.Button(
                            "进入核素选择",
                            style={"padding": "12px 36px", "fontSize": "1.05em"},
                        ),
                        href="/select-nuclide",
                    )
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

