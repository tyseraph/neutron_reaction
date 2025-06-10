def register_callbacks(app):
    from dash.dependencies import Output, Input
    import dash

    @app.callback(
        Output("url", "pathname", allow_duplicate=True),
        Input("back-to-simulation", "n_clicks"),
        prevent_initial_call=True
    )
    def back_to_simulation(n_clicks):
        if n_clicks:
            return "/theory-simulation"
        return dash.no_update
