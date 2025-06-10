# pages/select_nuclide.py

from dash import dcc, html
from dash import dash_table
import pandas as pd
from bs4 import BeautifulSoup
import os

# 加载数据
HTML_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase.html"))

def parse_nubase_html(html_file: str) -> pd.DataFrame:
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    table = soup.find("table")
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) == len(headers):
            rows.append(cells)
    return pd.DataFrame(rows, columns=headers)

def _load_dataframe():
    try:
        return parse_nubase_html(HTML_PATH)
    except Exception as e:
        print("加载 NUBASE HTML 表失败：", e)
        return None

NUCLIDE_DF = _load_dataframe()

# 页面布局
def layout():
    if NUCLIDE_DF is None or NUCLIDE_DF.empty:
        return html.Div([
            html.H3("核素选取"),
            html.P("无法加载 NUBASE 表，请检查 pandas 和 beautifulsoup4 是否安装，或检查 nubase.html 路径。"),
        ])
    return html.Div([
        html.H3("核素选取"),
        dash_table.DataTable(
            id="nuclide-table",
            columns=[{"name": "Nuclide", "id": "Nuclide"}],
            data=NUCLIDE_DF.to_dict("records"),
            row_selectable="multi",
            selected_rows=[],
            style_table={"overflowY": "auto", "maxHeight": "400px", "minWidth": "120px", "border": "1px solid #eee"},
            style_cell={"fontSize": "13px", "textAlign": "center", "padding": "3px 6px", "maxWidth": "120px"}
        ),
        html.Div(id="selected-nuclide", style={"fontWeight": "bold", "marginTop": "1rem"}),
        html.Button("进入模型参数选择", id="goto-model-params", n_clicks=0, disabled=True, style={"marginTop": "2rem"}),

        # 添加 dcc.Store 存储核素选择信息
        dcc.Store(id='store-selected-nuclide')
    ], style={"maxWidth": "350px", "padding": "2rem 1rem"})
