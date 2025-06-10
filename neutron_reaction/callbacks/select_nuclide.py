# callbacks/select_nuclide.py
import dash  # 确保导入 dash
from dash import Input, Output
from neutron_reaction.pages.select_nuclide import NUCLIDE_DF

def register_callbacks(app):
    @app.callback(
        Output('selected-nuclide', 'children'),
        Output('store-selected-nuclide', 'data'),
        Output('goto-model-params', 'disabled'),
        [Input('nuclide-table', 'selected_rows')]
    )
    def update_selected_nuclide(selected_rows):
        if not selected_rows:
            return "请选择一个或多个核素", None, True  # 如果没有选择核素，禁用按钮
        # 获取所选核素名称
        selected_nuclides = [NUCLIDE_DF.iloc[i]['Nuclide'] for i in selected_rows]
        # 将选择的核素存储到 store 中
        return f"已选择核素: {', '.join(selected_nuclides)}", selected_nuclides, False  # 启用按钮

    @app.callback(
        Output("url", "pathname", allow_duplicate=True),
        Input("goto-model-params", "n_clicks"),
        prevent_initial_call=True
    )
    def jump_to_model_params(n_clicks):
        if n_clicks:
            return "/model-params"  # 跳转到模型参数页面
        return dash.no_update  # 如果没有点击，保持当前页面不变