"""Dash application for the nuclear data evaluation platform."""

from neutron_reaction.layout import serve_layout
from neutron_reaction.pages import home, select_nuclide


def interactive_message() -> str:
    """Return a welcome message for the interactive platform."""
    return "Welcome to the Nuclear Data Evaluation Platform"


def create_dash_app():
    """Create and return the Dash application."""
    from dash import Dash
    from dash.dependencies import Input, Output

    app = Dash(__name__, suppress_callback_exceptions=True)
    app.layout = serve_layout

    @app.callback(Output("page-content", "children"), Input("url", "pathname"))
    def display_page(pathname: str):
        if pathname == "/select-nuclide":
            return select_nuclide.layout()
        return home.layout()

    return app


if __name__ == "__main__":
    application = create_dash_app()
    application.run_server(debug=True)

