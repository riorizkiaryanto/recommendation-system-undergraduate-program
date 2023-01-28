import warnings
warnings.filterwarnings("ignore")
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
from dash.html.Link import Link

from app import app, server
from templates import home, singlestage, others

app.layout = html.Div(
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ]
)

@app.callback(
    Output('page-content','children'),
    Input('url', 'pathname')
)

def display_page(pathname):
    if pathname == '/':
        return singlestage.layout
    elif pathname == '/home':
        return singlestage.layout
    # elif pathname == '/singlestage':
    #     return singlestage.layout
    elif pathname == '/rekomendasi':
        return others.layout
    # elif pathname is None:
    #     return "Loading..."
    else:
        return '404'

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, dev_tools_hot_reload=False)