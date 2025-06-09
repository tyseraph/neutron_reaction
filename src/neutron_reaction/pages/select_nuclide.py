import os
try:
    import pandas as pd  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    pd = None  # type: ignore

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    BeautifulSoup = None  # type: ignore

# === 1. 路径和解析函数 ===

HTML_PATH = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nubase.html")
)

def parse_nubase_html(html_file: str):
    """Parse the local NUBASE HTML table into a DataFrame.

    Returns ``None`` if the required dependencies are missing.
    """
    if pd is None or BeautifulSoup is None:
        return None
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    table = soup.find("table")
    headers = [th.get_text(strip=True) for th in table.find_all("th")]
    rows = []
    for tr in table.find_all("tr")[1:]:  # skip header row
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cells) == len(headers):
            rows.append(cells)
    return pd.DataFrame(rows, columns=headers)

def _load_dataframe():
    if pd is None or BeautifulSoup is None:
        return None
    try:
        return parse_nubase_html(HTML_PATH)
    except Exception as e:  # pragma: no cover - runtime warning only
        print("加载 NUBASE HTML 表失败：", e)
        return None

NUCLIDE_DF = _load_dataframe()

# === 2. 页面布局函数 ===

def layout():
    from dash import html, dash_table

    if NUCLIDE_DF is None:
        return html.Div([
            html.H3("核素选取"),
            html.P(
                "无法加载 NUBASE 表，请检查 pandas 和 beautifulsoup4 是否安装，或检查 nubase.html 路径。"
            ),
        ])
    return html.Div([
        html.H3("核素选取"),
        dash_table.DataTable(
            id="nuclide-table",
            columns=[{"name": c, "id": c} for c in NUCLIDE_DF.columns],
            data=NUCLIDE_DF.to_dict("records"),
            page_size=50,
            row_selectable="multi",
            filter_action="native",
            sort_action="native",
            style_table={"overflowX": "auto", "maxHeight": "700px", "overflowY": "auto"},
            style_cell={"fontSize": "12px", "textAlign": "center", "maxWidth": "150px"},
        ),
        html.Div(
            "请选择核素",
            id="nuclide-selected",
            style={"fontWeight": "bold", "marginTop": "1rem"},
        ),
    ])

# === 3. 回调注册函数 ===

def register_callbacks(app):
    from dash.dependencies import Input, Output

    @app.callback(
        Output("nuclide-selected", "children"),
        Input("nuclide-table", "selected_rows"),
    )
    def show_selected_nuclide(selected_rows):
        if NUCLIDE_DF is None or not selected_rows:
            return "请选择核素"

        selected_df = NUCLIDE_DF.iloc[selected_rows]
        if "Nuclide" in selected_df.columns:
            nuclides = ", ".join(selected_df["Nuclide"].tolist())
        else:
            nuclides = str(selected_df.to_dict("records"))
        return f"已选择：{nuclides}"
