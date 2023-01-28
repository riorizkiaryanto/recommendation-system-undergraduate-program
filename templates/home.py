import warnings
warnings.filterwarnings("ignore")
import dash
from dash import dcc
from dash import html

layout = html.Div(children=[
    html.Div(id="backgroundBox"),
    html.Div(id="secondBoxLayer"),
    html.Div(children=[
        html.H1("Sistem Rekomendasi", id="appName")
    ]),
    html.Div(children=[
        dcc.Link("Model rekomendasi", id="singeModelUrl", href='/singlestage')
    ])
])