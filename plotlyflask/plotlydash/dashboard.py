from dash import Dash
import dash_html_components as html

def init_dashboard(server):
    """Create a plotly Dash dashboard"""
    dash_app = Dash(server=server,
                    # routes_pathname_prefix="/model/",
                    external_stylesheets=["../static/style.css"])
 
    # Create Dash layout
    dash_app.layout = html.Div(id="backgroundBox")

    return dash_app.server