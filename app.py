import dash

app = dash.Dash(__name__, 
                external_stylesheets=["/assets/style.css"], 
                suppress_callback_exceptions=True)
app.config.suppress_callback_exceptions = True
server = app.server