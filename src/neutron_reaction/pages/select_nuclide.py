"""Nuclide selection page based on a configurable list of nuclides."""

from pathlib import Path

try:  # Optional import so tests pass even without pandas
    import pandas as pd
except Exception:  # pragma: no cover - used when dependency missing
    pd = None

from neutron_reaction.data.nuclides import generate_nuclide_data
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
ALLOWED_FILE = DATA_DIR / "allowed_nuclides.txt"
def _load_allowed_labels() -> list[str]:
    """Return the list of nuclide labels allowed for selection."""
    try:
        with open(ALLOWED_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:  # pragma: no cover - default to empty list
        return []
def _load_dataframe() -> "pd.DataFrame | None":
    if pd is None:
        return None
    df = pd.DataFrame(generate_nuclide_data())
    allowed = _load_allowed_labels()
    if allowed:
        df = df[df["label"].isin(allowed)]
    return df.reset_index(drop=True)
NUCLIDE_DF = _load_dataframe()
    if NUCLIDE_DF is None:
            html.P("缺少 pandas，无法加载核素列表"),
        columns=[{"name": c, "id": c} for c in NUCLIDE_DF.columns],
        data=NUCLIDE_DF.to_dict("records"),
        page_size=50,
    if NUCLIDE_DF is None:
            row = NUCLIDE_DF.iloc[selected_rows[0]]
            return f"已选择：{row['label']}"
            id="nuclide-dropdown",
            options=[
                {"label": f"{row['Nuclide']}", "value": idx}
                for idx, row in NUBASE_DF.iterrows()
            ],
            placeholder="选择核素，可多选",
            multi=True,
        )

    return html.Div(
        [
            html.H1("核素选择"),
            dcc.Link("返回首页", href="/", style={"marginRight": "1rem"}),
            html.Iframe(
                srcDoc=src_doc,
                style={"width": "100%", "height": "800px", "border": "none"},
            ),
            dropdown,
            html.Div(
                "请选择一个核素",
                id="nuclide-selected",
                style={"fontWeight": "bold", "marginTop": "1rem"},
            ),
        ]
    )


def register_callbacks(app):
    """Register callbacks for the nuclide selection page."""
    from dash.dependencies import Input, Output

    @app.callback(
        Output("nuclide-selected", "children"),
        Input("nuclide-dropdown", "value"),
    )
    def _show_dropdown_selection(value):
        if not value:
            return "请选择一个核素"

        if NUBASE_DF is not None:
            if not isinstance(value, list):
                value = [value]
            rows = [NUBASE_DF.iloc[v] for v in value]
            labels = [f"{i}-{row['Nuclide']}" for i, row in zip(value, rows)]
            return "已选择：" + ", ".join(labels)

        # Fallback when NUBASE table is unavailable
        if not isinstance(value, list):
            value = [value]
        return "已选择：" + ", ".join(value)
