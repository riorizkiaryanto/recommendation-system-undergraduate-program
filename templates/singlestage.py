import warnings
warnings.filterwarnings("ignore")
import joblib
from dash import dcc
from dash.dcc.Graph import Graph
import dash_html_components as html
from dash.dependencies import Output, Input
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from app import app, server

# import references list
list_sma, sma = LabelEncoder(), LabelEncoder()
list_sma = np.load('assets/dictReferences/sma_encoder_all.npy')
sma.classes_ = np.load('assets/dictReferences/sma_encoder_all.npy')

list_jurusan, jurusan = LabelEncoder(), LabelEncoder()
list_jurusan = np.load('assets/dictReferences/jurusan_encoder_all.npy')
jurusan.classes_ = np.load('assets/dictReferences/jurusan_encoder_all.npy')

list_hobi, hobi = LabelEncoder(), LabelEncoder()
list_hobi = np.load('assets/dictReferences/hobi_encoder_all.npy')
hobi.classes_ = np.load('assets/dictReferences/hobi_encoder_all.npy')

list_prodi, prodi = LabelEncoder(), LabelEncoder()
list_prodi = np.load('assets/dictReferences/prodi_encoder_all.npy')
prodi.classes_ = np.load('assets/dictReferences/prodi_encoder_all.npy')

def label_gender(gender):
    if gender == "Laki-laki":
        return 0
    elif gender == "Perempuan":
        return 1
    else:
        return 2

layout = html.Div(children=[
    html.Div(id="backgroundBox"),
    html.Div(id="secondBoxLayer"),
    html.Div(children=[
        html.H1("Sistem Rekomendasi", id="appName")
    ]),
    html.Div(children=[
        html.P("Pilih sesuai dengan profil Anda", id="labelCategoric")
    ]),
    html.Div(id="genderFilter", children=[
        dcc.Dropdown(
            id="gender",
            options=[
                    {'label': item, 'value': item} 
                    for item in ['Laki-laki', 'Perempuan', 'Tidak disebutkan']
                    ],
            value='',
            placeholder="Pilih jenis kelamin",
            clearable=True,
            searchable=True,
            className='dropdown',
            style = {'borderRadius': '20px'}
        )
    ]),
    html.Div(id="sekolahFilter", children=[
        dcc.Dropdown(
            id="sekolah",
            options=[
                    {'label': item, 'value': item} 
                    for item in list_sma
                    ],
            value='',
            placeholder="Pilih jenis sekolah",
            clearable=True,
            searchable=True,
            className='dropdown',
            style = {'borderRadius': '20px'}
        )
    ]),
    html.Div(id="jurusanFilter", children=[
        dcc.Dropdown(
            id="jurusan",
            options=[
                    {'label': item, 'value': item} 
                    for item in list_jurusan
                    ],
            value='',
            placeholder="Pilih jurusan sekolah",
            clearable=True,
            searchable=True,
            className='dropdown',
            style = {'borderRadius': '20px'}
        )
    ]),
    html.Div(id="hobiFilter", children=[
        dcc.Dropdown(
            id="hobi",
            options=[
                    {'label': item, 'value': item} 
                    for item in list_hobi
                    ],
            value='',
            placeholder="Pilih hobi",
            clearable=True,
            searchable=True,
            className='dropdown',
            style = {'borderRadius': '20px'}
        )
    ]),
    html.Div(id="bigWidthSeparator"),
    html.Div(id="sliderMTK", children=[
        html.I("Nilai rerata Matematika"),
        html.Br(),
        dcc.Slider(
            id="mtk",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderIndo", children=[
        html.I("Nilai rerata Bahasa Indonesia"),
        html.Br(),
        dcc.Slider(
            id="indo",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderIng", children=[
        html.I("Nilai rerata Bahasa Inggris"),
        html.Br(),
        dcc.Slider(
            id="ing",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderFis", children=[
        html.I("Nilai rerata Fisika"),
        html.Br(),
        dcc.Slider(
            id="fis",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderKim", children=[
        html.I("Nilai rerata Kimia"),
        html.Br(),
        dcc.Slider(
            id="kim",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderBio", children=[
        html.I("Nilai rerata Biologi"),
        html.Br(),
        dcc.Slider(
            id="bio",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderGeo", children=[
        html.I("Nilai rerata Geografi"),
        html.Br(),
        dcc.Slider(
            id="geo",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderEko", children=[
        html.I("Nilai rerata Ekonomi"),
        html.Br(),
        dcc.Slider(
            id="eko",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderSej", children=[
        html.I("Nilai rerata Sejarah"),
        html.Br(),
        dcc.Slider(
            id="sej",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.Div(id="sliderAg", children=[
        html.I("Nilai rerata Agama"),
        html.Br(),
        dcc.Slider(
            id="agm",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.I("Nilai rerata Ketrampilan Keahlian/Kejuruan", className="sliderKet"),
    html.Div(id="sliderKet", children=[
        html.Br(),
        dcc.Slider(
            id="kej",
            min=0,
            max=100,
            step=0,
            value=0,
            tooltip = {'always_visible': True, 'placement':'bottom'},
        ),    
    ]),
    html.P("Program studi sarjana yang paling cocok dengan Anda adalah", id="labelPred"),
    html.Div(id="otherRecommendation", children=[
        dcc.Link("Lihat rekomendasi lainnya", href="/rekomendasi", style={"textAlign": "center", "fontStyle": "italic", 
                                                              "fontSize": "12px", "color": "#00458E"})
    ]),
    # html.Div(id="backToHome", children=[
    #     dcc.Link("Kembali ke halaman utama", href="/", style={"textAlign": "center", "fontStyle": "italic", 
    #                                                           "fontSize": "12px", "color": "#FBFDFF"})
    # ]),
    html.Br(),
    html.Div(id="predictionText")
])

@app.callback(
    [Output("predictionText", "children")],
    [
        Input('gender', 'value'),
        Input('sekolah', 'value'),
        Input('jurusan', 'value'),
        Input('hobi', 'value'),
        Input('mtk', 'value'),
        Input('indo', 'value'),
        Input('ing', 'value'),
        Input('fis', 'value'),
        Input('kim', 'value'),
        Input('bio', 'value'),
        Input('eko', 'value'),
        Input('geo', 'value'),
        Input('sej', 'value'),
        Input('agm', 'value'),
        Input('kej', 'value'),
    ]
)

def classificationPredict(labelgender, labelsekolah, labeljurusan, labelhobi, mtk, indo, ing,
                            fis, kim, bio, eko, geo, sej, agm, kej):
    # load model classification
    model = joblib.load('assets/models/singlestage_rf.sav')

    if labelgender == '':
        labelgender = 'Tidak disebutkan'
    if labelsekolah == '':
        labelsekolah = 'Smu/Sma'
    if labeljurusan == '':
        labeljurusan = 'Ipa'
    if labelhobi == '':
        labelhobi = 'Lainnya'

    fixGender = label_gender(labelgender)
    fixSma = sma.transform([labelsekolah])[0]
    fixJurusan = jurusan.transform([labeljurusan])[0]
    fixHobi = hobi.transform([labelhobi])[0]

    # define input for categorical variables
    input = [fixGender, fixSma, fixJurusan, fixHobi]

    # define input for numerical variables
    input_num = [mtk, indo, ing, bio, fis, kim, 
             geo, sej, eko, agm, kej]

    # scaling input
    scaler = joblib.load('assets/models/singlestage_scaler.bin')

    input_num_scale = scaler.transform([input_num])
    
    input.extend(input_num_scale[0])
    
    pred = model.predict(np.reshape(input, (1,-1)))
    prob = model.predict_proba(np.reshape(input, (1,-1)))

    label_pred = prodi.inverse_transform([int(x) for x in pred])

    n = 10
    best_n = np.argsort(prob, axis=1)[:,-n:]
    top_n_labels = [model.classes_[i] for i in best_n]
    top_n_labels = prodi.inverse_transform([int(x) for x in top_n_labels[0]])
    top_n_probas = [prob[0][i] for i in best_n]

    df = pd.DataFrame({'Program Studi':top_n_labels, 'Probability':top_n_probas[0], 'y_label': [1]*n})
    df['Probability (%)'] = df['Probability'].apply(lambda x: round(x*100, 2))
    df = df.sort_values('Probability', ascending=False)

    if np.sum(input_num[4:14]) == 0:
        label_pred = ""
        return [label_pred]
    else:
        df.to_csv("assets/models/recommendation.csv", index=False)
        return [label_pred]