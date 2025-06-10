from dash import html, dcc
from neutron_reaction.components.sidebar import sidebar

def serve_layout():
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),   # 全局唯一的路由锚点
            sidebar(),                              # 侧边栏（你自己的 sidebar 组件）
            html.Div(
                id="page-content",                  # 页面内容区
                style={"marginLeft": "18rem", "padding": "2rem", "minHeight": "100vh"},
                # 这里加入了 minHeight: "100vh" 保证页面内容区的高度能够填充整个屏幕
            ),
        ]
    )
