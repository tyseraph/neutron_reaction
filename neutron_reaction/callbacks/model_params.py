# callbacks/model_params.py
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
from neutron_reaction.pages.model_params import model_reactions

def register_callbacks(app):
    # 更新下拉菜单内容，根据选择的模型类型
    @app.callback(
        Output('reaction-channel-list', 'children'),
        Output('store-model-and-reactions', 'data'),
        Output('selected-nuclide-display', 'children'),
        Output('model-dropdown', 'options'),  # 更新下拉菜单的选项
        [Input('model-checklist', 'value'),
         Input('store-selected-nuclide', 'data')]  # 获取选择的核素信息
    )
    def update_reactions(selected_models, selected_nuclide):
        if not selected_nuclide:
            return html.Div("请选择一个核素"), None, html.Div("没有选择核素"), []

        # 生成反应道列表
        reaction_channels = []
        dropdown_options = []

        # 遍历选择的模型
        for model in selected_models:
            # 获取模型对应的反应道
            channels = model_reactions.get(model, [])

            # 为每个模型生成一个反应道展示
            reaction_channels.append(html.Div([html.H4(model), html.Ul([html.Li(c) for c in channels])]))

            # 生成下拉菜单的选项，这里显示反应道而不是模型名称
            dropdown_options.extend([{'label': channel, 'value': channel} for channel in channels])

        # 存储选中的模型和反应道信息
        store_data = {
            'selected_models': selected_models,
            'reaction_channels': [model_reactions[model] for model in selected_models]
        }

        # 显示所选核素信息
        selected_nuclide_display = f"已选择的核素: {', '.join(selected_nuclide)}"

        # 返回更新的反应道、存储数据、显示核素信息和下拉菜单选项
        return reaction_channels, store_data, html.Div(selected_nuclide_display), dropdown_options

    # 点击按钮后跳转到数据评价页面
    @app.callback(
        Output('url', 'pathname'),
        [Input('go-to-data-evaluation', 'n_clicks')]
    )
    def navigate_to_data_evaluation(n_clicks):
        if n_clicks > 0:
            return '/data-evaluation'  # 当按钮被点击时，跳转到数据评价页面
        return dash.no_update
