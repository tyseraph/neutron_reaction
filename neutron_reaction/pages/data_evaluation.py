# pages/data_evaluation.py
import dash
from dash import dcc, html

# 从 model_params.py 中引入 model_reactions 字典
from neutron_reaction.pages.model_params import model_reactions

# 页面布局函数
def layout():
    return html.Div([
        html.H1("实验数据评价"),

        # 反应道下拉菜单
        dcc.Dropdown(
            id='reaction-dropdown',  # 选择反应道
            options=[],  # 初始时选项为空，回调会填充
            value=None,  # 默认值为空
            style={'width': '50%', 'margin': 'auto'}
        ),
        dcc.Store(id='store-model-and-reactions'),

        # 显示图表
        dcc.Graph(id='experiment-plot')
    ])
