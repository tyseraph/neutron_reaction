def register_callbacks(app):
    from dash.dependencies import Output, Input
    import dash

    @app.callback(
        Output("url", "pathname", allow_duplicate=True),
        Input("goto-results", "n_clicks"),
        prevent_initial_call=True
    )
    def goto_results(n_clicks):
        if n_clicks:
            return "/results"
        return dash.no_update
