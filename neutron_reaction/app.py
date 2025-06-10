# app.py
import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# 从页面模块导入布局（调用 layout() 函数）
from neutron_reaction.pages.select_nuclide import layout as select_nuclide_layout
from neutron_reaction.pages.model_params import layout as model_params_layout
from neutron_reaction.pages.data_evaluation import layout as data_evaluation_layout
from neutron_reaction.pages.theory_simulation import layout as theory_simulation_layout
from neutron_reaction.pages.results import layout as results_layout
from neutron_reaction.pages.home import layout as home_layout  # 导入首页的 layout 函数

# 从回调模块导入注册的回调
from neutron_reaction.callbacks.select_nuclide import register_callbacks as register_nuclide_callbacks
from neutron_reaction.callbacks.model_params import register_callbacks as register_model_params_callbacks
from neutron_reaction.callbacks.data_evaluation import register_callbacks as register_eval_callbacks
from neutron_reaction.callbacks.theory_simulation import register_callbacks as register_simulation_callbacks
from neutron_reaction.callbacks.results import register_callbacks as register_results_callbacks

# 从 components/sidebar.py 导入 sidebar 组件
from neutron_reaction.layout import serve_layout

def create_dash_app():
    # 初始化 Dash 应用
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

    # 设置页面布局，使用多页面路由
    app.layout = serve_layout

    # 根据 URL 路径来动态渲染页面
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/select-nuclide":
            return select_nuclide_layout()  # 调用 layout() 返回核素选择页面
        elif pathname == "/model-params":
            return model_params_layout()  # 调用 layout() 返回模型参数页面
        elif pathname == "/data-evaluation":
            return data_evaluation_layout()  # 调用 layout() 返回数据评价页面
        elif pathname == "/theory-simulation":
            return theory_simulation_layout()  # 调用 layout() 返回理论模拟页面
        elif pathname == "/results":
            return results_layout()  # 调用 layout() 返回结果页面
        return home_layout()  # 默认页面为首页，调用 layout() 函数返回首页布局

    # 注册回调函数
    register_nuclide_callbacks(app)  # 注册选择核素页面回调
    register_model_params_callbacks(app)  # 注册模型参数页面回调
    register_eval_callbacks(app)  # 注册数据评价页面回调
    register_simulation_callbacks(app)  # 注册理论模拟页面回调
    register_results_callbacks(app)  # 注册结果页面回调

    return app

if __name__ == "__main__":
    # 创建 Dash 应用并运行
    application = create_dash_app()
    application.run(debug=True, port=8060)
