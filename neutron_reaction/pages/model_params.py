# pages/model_params.py

from dash import dcc, html

# 定义不同模型影响的反应道
model_reactions = {
    '光学模型': ['总截面', '弹性截面', '弹性散射角分布'],
    '复合核+预平衡模型': ['光子出射截面', '中子出射截面', '质子出射截面'],
    '直接反应': ['去弹截面']
}

def layout():
    return html.Div([
        html.H3("选择模型类型", style={'textAlign': 'center', 'color': '#2c3e50'}),

        # 模型选择的复选框
        dcc.Checklist(
            id='model-checklist',
            options=[{'label': '光学模型', 'value': '光学模型'},
                     {'label': '复合核+预平衡模型', 'value': '复合核+预平衡模型'},
                     {'label': '直接反应', 'value': '直接反应'}],
            value=['光学模型'],  # 默认选择光学模型
            inline=True,  # 多选框水平排列
            style={'width': '50%', 'margin': 'auto'}
        ),

        # 反应道下拉菜单
        dcc.Dropdown(
            id='model-dropdown',  # 用于显示与选择的模型相关的反应道
            options=[],  # 初始选项为空，回调函数会填充
            value=None,  # 默认值为空
            style={'width': '50%', 'margin': 'auto'}
        ),

        # 用于显示选中的反应道
        html.Div(id='reaction-channel-list', style={'marginTop': '2rem'}),

        # 使用 dcc.Store 存储选中的模型和反应道信息
        dcc.Store(id='store-model-and-reactions'),
        # 添加 dcc.Store 存储选中的核素信息
        dcc.Store(id='store-selected-nuclide'),  # 必须添加这个 store 组件
        # 显示核素信息
        html.Div(id='selected-nuclide-display', style={'marginTop': '2rem'}),

        # 添加进入数据评价页面的按钮
        html.Div([
            html.Button("进入数据评价页面", id='go-to-data-evaluation', n_clicks=0, style={'marginTop': '2rem'})
        ], style={'textAlign': 'center'})
    ], style={'padding': '2rem', 'backgroundColor': '#ecf0f1'})
