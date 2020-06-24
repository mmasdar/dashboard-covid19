import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime

url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# Data can also be saved locally and read from local drive
# url_confirmed = 'time_series_covid19_confirmed_global.csv'
# url_deaths = 'time_series_covid19_deaths_global.csv'
# url_recovered = 'time_series_covid19_recovered_global.csv'

df_confirmed = pd.read_csv(url_confirmed)
df_deaths = pd.read_csv(url_deaths)
df_recovered = pd.read_csv(url_recovered)


colors = {
    'paper_color': '#393939',
    'text': '#E1E2E5',
    'plot_color': '#ffffff',
    'confirmed_text':'#3CA4FF',
    'deaths_text':'#f44336',
    'recovered_text':'#5A9E6F',
    'highest_case_bg':'#393939',
        }
        
divBorderStyle = {
    'backgroundColor' : '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9,
}
    

#DATA KAWASAN ASIA TENGGARA
#Data total kejadian Covid-19 di Indonesia
noToDisplay = 10

indonesia_confirmed   = df_confirmed.loc[df_confirmed['Country/Region'] == 'Indonesia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
timor_confirmed       = df_confirmed.loc[df_confirmed['Country/Region'] == 'Timor-Leste'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
brunei_confirmed      = df_confirmed.loc[df_confirmed['Country/Region'] == 'Brunei'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
myanmar_confirmed     = df_confirmed.loc[df_confirmed['Country/Region'] == 'Burma'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
kamboja_confirmed     = df_confirmed.loc[df_confirmed['Country/Region'] == 'Cambodia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
laos_confirmed        = df_confirmed.loc[df_confirmed['Country/Region'] == 'Laos'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
filipina_confirmed    = df_confirmed.loc[df_confirmed['Country/Region'] == 'Philippines'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
singapura_confirmed   = df_confirmed.loc[df_confirmed['Country/Region'] == 'Singapore'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
thailand_confirmed    = df_confirmed.loc[df_confirmed['Country/Region'] == 'Thailand'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
vietnam_confirmed     = df_confirmed.loc[df_confirmed['Country/Region'] == 'Vietnam'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
malaysia_confirmed    = df_confirmed.loc[df_confirmed['Country/Region'] == 'Malaysia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()


indonesia_deaths  = df_deaths.loc[df_deaths['Country/Region'] == 'Indonesia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
timor_deaths      = df_deaths.loc[df_deaths['Country/Region'] == 'Timor-Leste'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
brunei_deaths     = df_deaths.loc[df_deaths['Country/Region'] == 'Brunei'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
myanmar_deaths    = df_deaths.loc[df_deaths['Country/Region'] == 'Burma'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
kamboja_deaths    = df_deaths.loc[df_deaths['Country/Region'] == 'Cambodia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
laos_deaths       = df_deaths.loc[df_deaths['Country/Region'] == 'Laos'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
filipina_deaths   = df_deaths.loc[df_deaths['Country/Region'] == 'Philippines'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
singapura_deaths  = df_deaths.loc[df_deaths['Country/Region'] == 'Singapore'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
thailand_deaths   = df_deaths.loc[df_deaths['Country/Region'] == 'Thailand'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
vietnam_deaths    = df_deaths.loc[df_deaths['Country/Region'] == 'Vietnam'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
malaysia_deaths   = df_deaths.loc[df_deaths['Country/Region'] == 'Malaysia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()

indonesia_recovered  = df_recovered.loc[df_recovered['Country/Region'] == 'Indonesia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
timor_recovered      = df_recovered.loc[df_recovered['Country/Region'] == 'Timor-Leste'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
brunei_recovered     = df_recovered.loc[df_recovered['Country/Region'] == 'Brunei'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
myanmar_recovered    = df_recovered.loc[df_recovered['Country/Region'] == 'Burma'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
kamboja_recovered    = df_recovered.loc[df_recovered['Country/Region'] == 'Cambodia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
laos_recovered       = df_recovered.loc[df_recovered['Country/Region'] == 'Laos'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
filipina_recovered   = df_recovered.loc[df_recovered['Country/Region'] == 'Philippines'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
singapura_recovered  = df_recovered.loc[df_recovered['Country/Region'] == 'Singapore'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
thailand_recovered   = df_recovered.loc[df_recovered['Country/Region'] == 'Thailand'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
vietnam_recovered    = df_recovered.loc[df_recovered['Country/Region'] == 'Vietnam'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
malaysia_recovered   = df_recovered.loc[df_recovered['Country/Region'] == 'Malaysia'].drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()


jumlah_positif = (
                  indonesia_confirmed
                + timor_confirmed
                + brunei_confirmed
                + myanmar_confirmed
                + kamboja_confirmed
                + laos_confirmed
                + filipina_confirmed
                + singapura_confirmed
                + thailand_confirmed
                + vietnam_confirmed
                + malaysia_confirmed
                )

jumlah_kematian = ( 
                    indonesia_deaths
                   + timor_deaths
                   + brunei_deaths
                   + myanmar_deaths
                   + kamboja_deaths
                   + laos_deaths
                   + filipina_deaths
                   + singapura_deaths
                   + thailand_deaths
                   + vietnam_deaths
                   + malaysia_deaths 
                   )

jumlah_sembuh = ( 
                  indonesia_recovered
                 + timor_recovered
                 + brunei_recovered
                 + myanmar_recovered
                 + kamboja_recovered
                 + laos_recovered
                 + filipina_recovered
                 + singapura_recovered
                 + thailand_recovered
                 + vietnam_recovered
                 + malaysia_recovered
    
                )

x_jumlah_kematian = jumlah_sembuh.index

#data penambahan kasus Covid-19 harian Asia Tenggara
jumlah_positif_harian = (jumlah_positif - jumlah_positif.shift(1)).drop(jumlah_positif.index[0])
jumlah_kematian_harian = (jumlah_kematian - jumlah_kematian.shift(1)).drop(jumlah_kematian.index[0])
jumlah_sembuh_harian = (jumlah_sembuh - jumlah_sembuh.shift(1)).drop(jumlah_sembuh.index[0])

x_harian = jumlah_positif_harian.index


kasus_positif = [
                 indonesia_confirmed[-1], 
                 singapura_confirmed[-1],
                 filipina_confirmed[-1],
                 malaysia_confirmed[-1],
                 thailand_confirmed[-1],
                 timor_confirmed[-1],
                 brunei_confirmed[-1],
                 myanmar_confirmed[-1],
                 kamboja_confirmed[-1],
                 laos_confirmed[-1],
                 vietnam_confirmed[-1]
                 ]

kasus_kematian = [
                    indonesia_deaths[-1],
                    singapura_deaths[-1],
                    filipina_deaths[-1],
                    malaysia_deaths[-1],
                    thailand_deaths[-1],
                    timor_deaths[-1],
                    brunei_deaths[-1],
                    myanmar_deaths[-1],
                    kamboja_deaths[-1],
                    laos_deaths[-1],
                    vietnam_deaths[-1]
                  ]

kasus_sembuh = [ 
                  indonesia_recovered[-1],
                  singapura_recovered[-1],
                  filipina_recovered[-1],
                  malaysia_recovered[-1],
                  thailand_recovered[-1],
                  timor_recovered[-1],
                  brunei_recovered[-1],
                  myanmar_recovered[-1],
                  kamboja_recovered[-1],
                  laos_recovered[-1],
                  vietnam_recovered[-1]
                ]

#Kasus dalam 24 jam terakhir
kasus_positif_24h = [
                 indonesia_confirmed[-1] - indonesia_confirmed[-2], 
                 singapura_confirmed[-1] - singapura_confirmed[-2],
                 filipina_confirmed[-1] - filipina_confirmed[-2],
                 malaysia_confirmed[-1] - malaysia_confirmed[-2],
                 thailand_confirmed[-1] - thailand_confirmed[-2],
                 timor_confirmed[-1] - timor_confirmed[-2],
                 brunei_confirmed[-1] - brunei_confirmed[-2],
                 myanmar_confirmed[-1] - myanmar_confirmed[-2],
                 kamboja_confirmed[-1] - kamboja_confirmed[-2],
                 laos_confirmed[-1] - laos_confirmed[-2],
                 vietnam_confirmed[-1] - vietnam_confirmed[-2]
                 ]

kasus_kematian_24h = [
                    indonesia_deaths[-1] - indonesia_deaths[-2],
                    singapura_deaths[-1] - singapura_deaths[-2],
                    filipina_deaths[-1] - filipina_deaths[-2],
                    malaysia_deaths[-1] - malaysia_deaths[-2],
                    thailand_deaths[-1] - thailand_deaths[-2],
                    timor_deaths[-1] - timor_deaths[-2],
                    brunei_deaths[-1] - brunei_deaths[-2],
                    myanmar_deaths[-1] - myanmar_deaths[-2],
                    kamboja_deaths[-1] - kamboja_deaths[-2],
                    laos_deaths[-1] - laos_deaths[-2],
                    vietnam_deaths[-1] - vietnam_deaths[-2]
                  ]

kasus_sembuh_24h = [ 
                  indonesia_recovered[-1] - indonesia_recovered[-2],
                  singapura_recovered[-1] - singapura_recovered[-2],
                  filipina_recovered[-1] - filipina_recovered[-2],
                  malaysia_recovered[-1] - malaysia_recovered[-2],
                  thailand_recovered[-1] - thailand_recovered[-2],
                  timor_recovered[-1] - timor_recovered[-2],
                  brunei_recovered[-1] - brunei_recovered[-2],
                  myanmar_recovered[-1] - myanmar_recovered[-2],
                  kamboja_recovered[-1] - kamboja_recovered[-2],
                  laos_recovered[-1] - laos_recovered[-2],
                  vietnam_recovered[-1] - vietnam_recovered[-2]
                ]

label_negara = [ 
                'INDONESIA',
                'SINGAPURA',
                'FILIPINA',
                'MALAYSIA',
                'THAILAND',
                'TIMOR LESTE',
                'BRUNEI DARUSSALAM',
                'MYANMAR',
                'KAMBOJA',
                'LAOS',
                'VIETNAM'
                ]


cars = {'negara': label_negara,
        'positif': kasus_positif,
        'meninggal': kasus_kematian,
        'sembuh': kasus_sembuh,
        'positif_24h': kasus_positif_24h,
        'meninggal_24h': kasus_kematian_24h,
        'sembuh_24h': kasus_sembuh_24h
        }

data_asia_tenggara = pd.DataFrame(cars, columns = ['negara', 'positif', 'meninggal', 'sembuh', 'positif_24h', 'meninggal_24h', 'sembuh_24h'])
data_asia_tenggara



def high_cases(countryname,total,single,color_word='#63b6ff',confirmed_total=1,deaths = False,):

    if deaths:

        percent = (total/confirmed_total)*100
        return html.P([ html.Span(countryname + ' | ' + f"{int(total):,d}",
                             style={'backgroundColor': colors['highest_case_bg'], 'borderRadius': '6px',}),
                    html.Span(' +' + f"{int(single):,d}",
                             style={'color': color_word,'margin':2,'fontWeight': 'bold','fontSize': 14,}),
                    html.Span(f' ({percent:.2f}%)',
                             style={'color': color_word,'margin':2,'fontWeight': 'bold','fontSize': 14,}),
                   ],
                  style={
                        'textAlign': 'center',
                        'color': 'rgb(200,200,200)',
                        'fontsize':12,
                        }       
                )

    return html.P([ html.Span(countryname + ' | ' + f"{int(total):,d}",
                        style={'backgroundColor': colors['highest_case_bg'], 'borderRadius': '6px',}),
            html.Span(' +' + f"{int(single):,d}",
                        style={'color': color_word,'margin':2,'fontWeight': 'bold','fontSize': 14,}),
            ],
            style={
                'textAlign': 'center',
                'color': 'rgb(200,200,200)',
                'fontsize':12,
                }       
        )


confirm_cases = []
for i in range(noToDisplay):
    confirm_cases.append(high_cases(data_asia_tenggara.iloc[i,0], data_asia_tenggara.iloc[i,1], data_asia_tenggara.iloc[i,4]))

deaths_cases = []
for i in range(noToDisplay):
    deaths_cases.append(high_cases(data_asia_tenggara.iloc[i,0],data_asia_tenggara.iloc[i,2],data_asia_tenggara.iloc[i,5],'#ff3b4a',True))

'''
confirm_cases_24hrs = []
for i in range(noToDisplay):
    confirm_cases_24hrs.append(high_cases(df_confirmed_sorted_total.sort_values(by=df_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,0],
                                            df_confirmed_sorted_total.sort_values(by=df_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,1],
                                            df_confirmed_sorted_total.sort_values(by=df_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,2],
                                            ))

deaths_cases_24hrs = []
for i in range(noToDisplay):
    deaths_cases_24hrs.append(high_cases(df_deaths_confirmed_sorted_total.sort_values(by=df_deaths_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,0],
                                            df_deaths_confirmed_sorted_total.sort_values(by=df_deaths_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,1],
                                            df_deaths_confirmed_sorted_total.sort_values(by=df_deaths_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,3],
                                            '#ff3b4a',
                                            df_deaths_confirmed_sorted_total.sort_values(by=df_deaths_confirmed_sorted_total.columns[-1], ascending=False).iloc[i,2],
                                            True))
'''

tab_3_layout = html.Div([
            html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x_jumlah_kematian, 'y' : jumlah_positif, 'type' : 'line', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : x_jumlah_kematian, 'y' : jumlah_kematian, 'type' : 'line', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}},
                            {'x' : x_jumlah_kematian, 'y' : jumlah_sembuh, 'type' : 'line', 'name' : 'Sembuh', 'marker' : {'color' : colors['recovered_text']}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'Grafik Total Perkembangan Covid-19 di Kawasan Asia Tenggara',
                            'legend' : dict(x=0.15, y=0.9)
                        }
                    })
                ], className="row", style={"margin": "1% 3%"}),

        html.Div([
            html.Div([
                html.H4(children='Total Positif: ',
                       style={
                           'textAlign': 'center',
                           'color': colors['confirmed_text'],
                       }
                       ),
                html.P(f"{jumlah_positif[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['confirmed_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Penambahan (24 Jam): +' + f"{jumlah_positif[-1] - jumlah_positif[-2]:,d}"
                       + ' (' + str(round(((jumlah_positif[-1] - jumlah_positif[-2])/jumlah_positif[-1])*100, 2)) + '%)',
                       style={
                    'textAlign': 'center',
                    'color': colors['confirmed_text'],
                }
                ),
            ],
                style=divBorderStyle,
                className='four columns',
            ),
            html.Div([
                html.H4(children='Total Meninggal: ',
                       style={
                           'textAlign': 'center',
                           'color': colors['deaths_text'],
                       }
                       ),
                html.P(f"{jumlah_kematian[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['deaths_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kematian: ' + str(round(jumlah_kematian[-1]/jumlah_positif[-1] * 100, 3)) + '%',
                       style={
                    'textAlign': 'center',
                    'color': colors['deaths_text'],
                }
                ),
            ],
                style=divBorderStyle,
                className='four columns'),
            html.Div([
                html.H4(children='Total Sembuh: ',
                       style={
                           'textAlign': 'center',
                           'color': colors['recovered_text'],
                       }
                       ),
                html.P(f"{jumlah_sembuh[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['recovered_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kesembuhan: ' + str(round(jumlah_sembuh[-1]/jumlah_positif[-1] * 100, 3)) + '%',
                       style={
                    'textAlign': 'center',
                    'color': colors['recovered_text'],
                }
                ),
            ],
                style=divBorderStyle,
                className='four columns'),
        ], className='row', style={"margin": "2% 3%"}),


                html.Div([
                    html.H6('Grafik Harian Perkembangan Covid-19 di Kawasan Asia Tenggara', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x_harian, 'y' : jumlah_positif_harian, 'type' : 'line', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : x_harian, 'y' : jumlah_kematian_harian, 'type' : 'line', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}},
                            {'x' : x_harian, 'y' : jumlah_sembuh_harian, 'type' : 'line', 'name' : 'Sembuh', 'marker' : {'color' : colors['recovered_text']}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'legend' : dict(x=0.15, y=0.9)
                        }
                    })
                ], className="row", style={"margin": "1% 3%"}),

    ],className='row', style={'backgroundColor': '#2D2D2D'}),


html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : label_negara, 'y' : kasus_positif, 'type' : 'bar', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : label_negara, 'y' : kasus_sembuh, 'type' : 'bar', 'name' : 'Sembuh', 'marker' : {'color' : colors['recovered_text']}},
                            {'x' : label_negara, 'y' : kasus_kematian, 'type' : 'bar', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'Negara dengan Konfirmasi Positif Tertinggi',
                            'legend' : dict(x=0.7, y=0.9)
                        }
                    })
                ], className="row", style={"margin": "1% 3%"})
            ], className="row", style={'backgroundColor': '#2D2D2D'}),


                html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : label_negara, 'y' : data_asia_tenggara.iloc[0:, 1], 'type' : 'bar', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : label_negara, 'y' : data_asia_tenggara.iloc[0:, 4], 'type' : 'bar', 'name' : '+24h', 'marker' : {'color' : 'white'}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'Negara dengan Konfirmasi Positif Tertinggi',
                            'legend' : dict(x=0.7, y=0.9)
                        }
                    })
                ], className="nine columns"),

                html.Div([
                    html.P([html.Span('Kasus Positif Tertinggi: ',),
                    html.Br(),
                    html.Span(' + 24 Jam Terakhir',
                             style={'color': 'white',
                             'fontWeight': 'bold','fontSize': 14,})
                    ],
                    style={
                        'textAlign': 'center',
                        'color': 'rgb(200,200,200)',
                        'fontsize':12,
                        'backgroundColor':'#3B5998',
                        'borderRadius': '12px',
                        'fontSize': 17,
                        }       
                ),
                html.P(confirm_cases),
            ], className="three columns"),
            ], className="row", style={"margin": "1% 3%"}),

        html.Div([
                
                html.Div([
                    html.P([html.Span('Negara Kematian Tertinggi',),
                    html.Br(),
                    html.Span(' + 24 Jam Terakhir',
                             style={'color': 'white',
                             'fontWeight': 'bold','fontSize': 14,})
                    ],
                    style={
                        'textAlign': 'center',
                        'color': 'rgb(200,200,200)',
                        'fontsize':12,
                        'backgroundColor':'#ab2c1a',
                        'borderRadius': '12px',
                        'fontSize': 17,
                        }       
                ),
                html.P(deaths_cases),
            ], className="three columns"),

                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : label_negara, 'y' : data_asia_tenggara.iloc[0:, 2], 'type' : 'bar', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}},
                            {'x' : label_negara, 'y' : data_asia_tenggara.iloc[0:, 5], 'type' : 'bar', 'name' : '+24h', 'marker' : {'color' : 'white'}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'Negara dengan Konfirmasi Positif Tertinggi',
                            'legend' : dict(x=0.7, y=0.9)
                        }
                    })
                ], className="nine columns")
            ], className="row", style={"margin": "2% 3%"})
])



