# callbacks/data_evaluation.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# 从 model_params.py 中引入 model_reactions 字典
from neutron_reaction.pages.model_params import model_reactions

# 回调函数：根据选择的反应道更新图表
def register_callbacks(app):
    @app.callback(
        Output('reaction-dropdown', 'options'),
        [Input('store-model-and-reactions', 'data')]  # 获取存储的模型和反应道数据
    )
    def update_reaction_dropdown(store_data):
        if store_data:
            # 获取反应道信息（从存储中读取）
            selected_models = store_data.get('selected_models', [])
            reaction_channels = []

            for model in selected_models:
                # 获取每个模型的反应道
                channels = model_reactions.get(model, [])
                reaction_channels.extend([{'label': channel, 'value': channel} for channel in channels])

            return reaction_channels
        return []  # 如果没有存储的数据，返回空选项

    @app.callback(
        Output('experiment-plot', 'figure'),
        [Input('reaction-dropdown', 'value')]  # 获取选择的反应道
    )
    def update_plot(selected_reaction):
        if selected_reaction:
            # 在这里你可以基于选中的反应道绘制图表
            # 例如，绘制能量与截面之间的关系
            fig = go.Figure()

            # 根据选中的反应道绘制不同的数据
            fig.add_trace(go.Scatter(
                x=[1, 2, 3, 4],  # 示例数据，实际应用时请替换为实际的实验数据
                y=[10, 11, 12, 13],
                mode='lines+markers',
                name=f'{selected_reaction}'
            ))

            fig.update_layout(title=f"能量 vs 截面 ({selected_reaction})", xaxis={'title': '能量'},
                              yaxis={'title': '截面'})

            return fig
        return go.Figure()  # 如果没有选择反应道，返回空图表
