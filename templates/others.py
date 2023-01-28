import warnings
warnings.filterwarnings("ignore")
from dash import dcc
from dash.dcc.Graph import Graph
import dash_html_components as html
from dash.dependencies import Output, Input
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from app import app, server

layout = html.Div(children=[
    html.Div(id="backgroundBox"),
    html.Div(id="secondBoxLayer"),
    html.Div(children=[
        html.H1("Sistem Rekomendasi", id="appName")
    ]),
    html.Div(
        html.P("Berikut adalah rekomendasi program studi sarjana lainnya", id="otherText")
    ),
    html.Div(
        dcc.Graph(id="graph")
    ),
    # html.Div(id="backToHome", children=[
    #     dcc.Link("Kembali ke halaman utama", href="/", style={"textAlign": "center", "fontStyle": "italic", 
    #                                                           "fontSize": "12px", "color": "#FBFDFF"})
    # ]),
    html.Div(id="backToSimulation", children=[
        dcc.Link("Kembali ke simulasi", href="/", style={"textAlign": "center", "fontStyle": "italic", 
                                                              "fontSize": "12px", "color": "#00458E"})
    ]),
])

@app.callback(
    Output('graph','figure'),
    Input('url', 'pathname')
)

def updateGraph(pathname):
    if pathname=="/rekomendasi":
        df = pd.read_csv("assets/models/recommendation.csv")

        # fig = px.bar(df, x="Probability", y="Program Studi", orientation='h')

        n = len(df)

        prob_df = df['Probability (%)'].tolist()
        color_set = []
        size_adj = []
        prev_num = 100
        for i in range(n):
            color_set.append(i)
            if i == 0:
                size_adj.append(100)
            else:
                divLabel = prob_df[i] - prob_df[i-1]
                size_adj.append(prev_num - divLabel)

        fig = go.Figure(data=go.Scatter(
            x=df['Program Studi'].tolist(),
            y=df['Probability (%)'].tolist(),
            mode='markers',
            marker=dict(size=size_adj,
                    color=color_set),
            hovertemplate =
            '<b>Program Studi</b>: %{x}'+
            '<br><b>Probability</b>: %{y:.2f}%<br>'+
            "<extra></extra>",
            showlegend=False
        ))

        fig.update_layout(title=str(n) + " Rekomendasi Program Studi Lain",
                    yaxis_title="Probability (%)",
                    xaxis_title="Program Studi")

        return fig
    else:
        fig = go.Figure()
        return fig