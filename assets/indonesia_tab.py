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

#########################################################################################
# Data preprocessing for getting useful data and shaping data compatible to plotly plot
#########################################################################################


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
    
    
#Data total kejadian Covid-19 di Indonesia
indonesia_confirmed_1     = df_confirmed.loc[df_confirmed['Country/Region'] == 'Indonesia']
indonesia_deaths_1        = df_deaths.loc[df_deaths['Country/Region'] == 'Indonesia']
indonesia_recovered_1     = df_recovered.loc[df_recovered['Country/Region'] == 'Indonesia']

indonesia_confirmed     = indonesia_confirmed_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T
indonesia_deaths        = indonesia_deaths_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T
indonesia_recovered     = indonesia_recovered_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T

xxx = indonesia_confirmed.index

#merubah data indonesia menjadi array agar dapat dilakukan operasi matematis
indonesia_confirmed_array     = indonesia_confirmed_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
indonesia_deaths_array        = indonesia_deaths_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()
indonesia_recovered_array     = indonesia_recovered_1.drop(['Province/State','Country/Region','Lat','Long'],axis=1).sum()

x_array = indonesia_deaths_array.index


#data penambahan kasus Covid-19 harian Indonesia
indonesia_confirmed_shift   = (indonesia_confirmed_array - indonesia_confirmed_array.shift(1)).drop(indonesia_confirmed_array.index[0])
indonesia_deaths_shift      = (indonesia_deaths_array - indonesia_deaths_array.shift(1)).drop(indonesia_deaths_array.index[0])
indonesia_recovered_shift   = (indonesia_recovered_array - indonesia_recovered_array.shift(1)).drop(indonesia_recovered_array.index[0])

x_shift = indonesia_confirmed_shift.index


 

tab_3_layout = html.Div([
            html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x_array, 'y' : indonesia_confirmed_array, 'type' : 'line', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : x_array, 'y' : indonesia_deaths_array, 'type' : 'line', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}},
                            {'x' : x_array, 'y' : indonesia_recovered_array, 'type' : 'line', 'name' : 'Sembuh', 'marker' : {'color' : colors['recovered_text']}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'title' : 'Grafik Total Perkembangan Covid-19 di Indonesia',
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
                html.P(f"{indonesia_confirmed_array[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['confirmed_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Penambahan (24 Jam): +' + f"{indonesia_confirmed_array[-1] - indonesia_confirmed_array[-2]:,d}"
                       + ' (' + str(round(((indonesia_confirmed_array[-1] - indonesia_confirmed_array[-2])/indonesia_confirmed_array[-1])*100, 2)) + '%)',
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
                html.P(f"{indonesia_deaths_array[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['deaths_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kematian: ' + str(round(indonesia_deaths_array[-1]/indonesia_confirmed_array[-1] * 100, 3)) + '%',
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
                html.P(f"{indonesia_recovered_array[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['recovered_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kesembuhan: ' + str(round(indonesia_recovered_array[-1]/indonesia_confirmed_array[-1] * 100, 3)) + '%',
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
                html.Div([
                    html.H6('Tingkat Kematian Pasien Covid-19', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                        id='tab_baru_1',
                        figure={
                            'data': [
                            {'x' : x_array, 'y' : indonesia_deaths_array, 'type' : 'bar', 'marker' : {'color' : colors['deaths_text']}},
                            ],
                            'layout': {
                                        'plot_bgcolor' : colors['paper_color'],
                                        'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']}

                            #'title' : 'Tingkat Kematian Pasien Covid-19'
                            }
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Tingkat Kesembuhan Pasien Covid-19', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                        id='tab_baru_2',
                        figure={
                            'data': [
                            {'x' : x_array, 'y' : indonesia_recovered_array, 'type' : 'bar', 'marker' : {'color' : colors['recovered_text']}},
                            ],
                            'layout': {
                                        'plot_bgcolor' : colors['paper_color'],
                                        'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']}

                            #'title' : 'Tingkat Kesembuhan Pasien Covid-19'
                            }
                        }
                    )
                ], className="six columns"),
                ], className="row",style={"margin": "1% 3%"}),

                html.Div([
                    html.H6('Grafik Harian Perkembangan Covid-19 di Indonesia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x_array, 'y' : indonesia_confirmed_shift, 'type' : 'line', 'name' : 'Positif', 'marker' : {'color' : colors['confirmed_text']}},
                            {'x' : x_array, 'y' : indonesia_deaths_shift, 'type' : 'line', 'name' : 'Meninggal', 'marker' : {'color' : colors['deaths_text']}},
                            {'x' : x_array, 'y' : indonesia_recovered_shift, 'type' : 'line', 'name' : 'Sembuh', 'marker' : {'color' : colors['recovered_text']}}
                        ],
                        'layout' : {
                            'plot_bgcolor' : colors['paper_color'],
                            'paper_bgcolor' : colors['paper_color'],
                            'font' : {'color' : colors['text']},
                            'legend' : dict(x=0.15, y=0.9)
                        }
                    })
                ], className="row", style={"margin": "1% 3%"}),

    ],className='row', style={'backgroundColor': '#2D2D2D'})
               
])



