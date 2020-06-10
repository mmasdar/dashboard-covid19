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
def df_move1st_sg(df_t):

    #Moving Singapore to the first row in the datatable
    df_t["new"] = range(1,len(df_t)+1)
    df_t.loc[df_t[df_t['Country/Region'] == 'Indonesia'].index.values,'new'] = 0
    df_t = df_t.sort_values("new").drop('new', axis=1)
    return df_t


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
    
# Total cases
df_confirmed_total = df_confirmed.iloc[:, 4:].sum(axis=0)
df_deaths_total = df_deaths.iloc[:, 4:].sum(axis=0)
df_recovered_total = df_recovered.iloc[:, 4:].sum(axis=0)

#Daily Cases Global
df_confirmed_daily = (df_confirmed_total - df_confirmed_total.shift(1)).drop(df_confirmed_total.index[0])
df_deaths_daily = (df_deaths_total - df_deaths_total.shift(1)).drop(df_deaths_total.index[0])
df_recovered_daily = (df_recovered_total - df_recovered_total.shift(1)).drop(df_recovered_total.index[0])

# modified deaths dataset for mortality rate calculation
df_deaths_confirmed=df_deaths.copy()
df_deaths_confirmed['confirmed'] = df_confirmed.iloc[:,-1]

#Sorted - df_deaths_confirmed_sorted is different from others, as it is only modified later. Careful of it dataframe structure
df_deaths_confirmed_sorted = df_deaths_confirmed.sort_values(by=df_deaths_confirmed.columns[-2], ascending=False)[['Country/Region',df_deaths_confirmed.columns[-2],df_deaths_confirmed.columns[-1]]]
df_recovered_sorted = df_recovered.sort_values(by=df_recovered.columns[-1], ascending=False)[['Country/Region',df_recovered.columns[-1]]]
df_confirmed_sorted = df_confirmed.sort_values(by=df_confirmed.columns[-1], ascending=False)[['Country/Region',df_confirmed.columns[-1]]]

#Single day increase
df_deaths_confirmed_sorted['24hr'] = df_deaths_confirmed_sorted.iloc[:,-2] - df_deaths.sort_values(by=df_deaths.columns[-1], ascending=False)[df_deaths.columns[-2]]
df_recovered_sorted['24hr'] = df_recovered_sorted.iloc[:,-1] - df_recovered.sort_values(by=df_recovered.columns[-1], ascending=False)[df_recovered.columns[-2]]
df_confirmed_sorted['24hr'] = df_confirmed_sorted.iloc[:,-1] - df_confirmed.sort_values(by=df_confirmed.columns[-1], ascending=False)[df_confirmed.columns[-2]]

#Aggregate the countries with different province/state together
df_deaths_confirmed_sorted_total = df_deaths_confirmed_sorted.groupby('Country/Region').sum()
df_deaths_confirmed_sorted_total=df_deaths_confirmed_sorted_total.sort_values(by=df_deaths_confirmed_sorted_total.columns[0], ascending=False).reset_index()
df_recovered_sorted_total = df_recovered_sorted.groupby('Country/Region').sum()
df_recovered_sorted_total=df_recovered_sorted_total.sort_values(by=df_recovered_sorted_total.columns[0], ascending=False).reset_index()
df_confirmed_sorted_total = df_confirmed_sorted.groupby('Country/Region').sum()
df_confirmed_sorted_total=df_confirmed_sorted_total.sort_values(by=df_confirmed_sorted_total.columns[0], ascending=False).reset_index()

#Modified recovery csv due to difference in number of rows. Recovered will match ['Province/State','Country/Region']column with Confirmed ['Province/State','Country/Region']
df_recovered['Province+Country'] = df_recovered[['Province/State','Country/Region']].fillna('nann').agg('|'.join,axis=1)
df_confirmed['Province+Country'] = df_confirmed[['Province/State','Country/Region']].fillna('nann').agg('|'.join,axis=1)
df_recovered_fill = df_recovered
df_recovered_fill.set_index("Province+Country")
df_recovered_fill.set_index("Province+Country").reindex(df_confirmed['Province+Country'])
df_recovered_fill = df_recovered_fill.set_index("Province+Country").reindex(df_confirmed['Province+Country']).reset_index()

#split Province+Country back into its respective columns
new = df_recovered_fill["Province+Country"].str.split("|", n = 1, expand = True)
df_recovered_fill['Province/State']=new[0]
df_recovered_fill['Country/Region']=new[1]
df_recovered_fill['Province/State'].replace('nann','NaN')

#drop 'Province+Country' for all dataset
df_confirmed.drop('Province+Country',axis=1,inplace=True)
df_recovered.drop('Province+Country',axis=1,inplace=True)
df_recovered_fill.drop('Province+Country',axis=1,inplace=True)

# Data preprocessing for times series countries graph display 
# create temp to store sorting arrangement for all confirm, deaths and recovered.
df_confirmed_sort_temp = df_confirmed.sort_values(by=df_confirmed.columns[-1], ascending=False)

df_confirmed_t = df_move1st_sg(df_confirmed_sort_temp)
df_confirmed_t['Province+Country'] = df_confirmed_t[['Province/State','Country/Region']].fillna('nann').agg('|'.join,axis=1)
df_confirmed_t=df_confirmed_t.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T

df_deaths_t = df_deaths.reindex(df_confirmed_sort_temp.index)
df_deaths_t = df_move1st_sg(df_deaths_t)
df_deaths_t['Province+Country'] = df_deaths_t[['Province/State','Country/Region']].fillna('nann').agg('|'.join,axis=1)
df_deaths_t=df_deaths_t.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T

# take note use reovered_fill df
df_recovered_t = df_recovered_fill.reindex(df_confirmed_sort_temp.index)
df_recovered_t = df_move1st_sg(df_recovered_t)
df_recovered_t['Province+Country'] = df_recovered_t[['Province/State','Country/Region']].fillna('nann').agg('|'.join,axis=1)
df_recovered_t=df_recovered_t.drop(['Province/State','Country/Region','Lat','Long'],axis=1).T

df_confirmed_t.columns = df_confirmed_t.iloc[-1]
df_confirmed_t = df_confirmed_t.drop('Province+Country')

df_deaths_t.columns = df_deaths_t.iloc[-1]
df_deaths_t = df_deaths_t.drop('Province+Country')

df_recovered_t.columns = df_recovered_t.iloc[-1]
df_recovered_t = df_recovered_t.drop('Province+Country')

df_confirmed_t.index=pd.to_datetime(df_confirmed_t.index)
df_deaths_t.index=pd.to_datetime(df_confirmed_t.index)
df_recovered_t.index=pd.to_datetime(df_confirmed_t.index)

df_confirmed_t = (df_confirmed_t - df_confirmed_t.shift(1)).drop(df_confirmed_t.index[0])
df_deaths_t = (df_deaths_t - df_deaths_t.shift(1)).drop(df_deaths_t.index[0])
df_recovered_t = (df_recovered_t - df_recovered_t.shift(1)).drop(df_recovered_t.index[0])

x=df_confirmed_total.index
y1=df_confirmed_total
y2=df_deaths_total
y3=df_recovered_total

x_daily  = df_confirmed_daily.index
y1_daily = df_confirmed_daily
y2_daily = df_deaths_daily
y3_daily = df_recovered_daily

#Data untuk negara dengan kasus tertinggi dan kenaikannya dalam 24 jam
noToDisplay = 12

data_baru = df_confirmed_sorted_total.head(noToDisplay)
negara_nama = data_baru.iloc[0:noToDisplay,0]
negara_kasus = data_baru.iloc[0:noToDisplay,1]
negara_penambahan = data_baru.iloc[0:noToDisplay,2]

meninggal_data_baru = df_deaths_confirmed_sorted_total.head(noToDisplay)
meninggal_negara_nama = meninggal_data_baru.iloc[0:noToDisplay,0]
meninggal_negara_kasus = meninggal_data_baru.iloc[0:noToDisplay,1]
meninggal_negara_penambahan = meninggal_data_baru.iloc[0:noToDisplay,3]


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
    confirm_cases.append(high_cases(df_confirmed_sorted_total.iloc[i,0],df_confirmed_sorted_total.iloc[i,1],df_confirmed_sorted_total.iloc[i,2]))

deaths_cases = []
for i in range(noToDisplay):
    deaths_cases.append(high_cases(df_deaths_confirmed_sorted_total.iloc[i,0],df_deaths_confirmed_sorted_total.iloc[i,1],df_deaths_confirmed_sorted_total.iloc[i,3],'#ff3b4a',df_deaths_confirmed_sorted_total.iloc[i,2],True))

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

tab_3_layout = html.Div([
            html.Div([
                html.Div([
                    #html.H6('Grafik Perkembangan Covid-19 di Seluruh Dunia', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x, 'y' : y1, 'type' : 'line', 'name' : 'Positif', 'marker' : {'color' : 'blue'}},
                            {'x' : x, 'y' : y2, 'type' : 'line', 'name' : 'Meninggal', 'marker' : {'color' : 'red'}},
                            {'x' : x, 'y' : y3, 'type' : 'line', 'name' : 'Sembuh', 'marker' : {'color' : 'green'}}
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
                html.P(f"{df_confirmed_total[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['confirmed_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Penambahan (24 Jam): +' + f"{df_confirmed_total[-1] - df_confirmed_total[-2]:,d}"
                       + ' (' + str(round(((df_confirmed_total[-1] - df_confirmed_total[-2])/df_confirmed_total[-1])*100, 2)) + '%)',
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
                html.P(f"{df_deaths_total[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['deaths_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kematian: ' + str(round(df_deaths_total[-1]/df_confirmed_total[-1] * 100, 3)) + '%',
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
                html.P(f"{df_recovered_total[-1]:,d}",
                       style={
                    'textAlign': 'center',
                    'color': colors['recovered_text'],
                    'fontSize': 30,
                }
                ),
                html.P('Tingkat Kesembuhan: ' + str(round(df_recovered_total[-1]/df_confirmed_total[-1] * 100, 3)) + '%',
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
                            {'x' : x, 'y' : y2, 'type' : 'bar', 'marker' : {'color' : 'red'}},
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
                            {'x' : x, 'y' : y3, 'type' : 'bar', 'marker' : {'color' : 'green'}},
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
                    html.H6('Grafik Harian Perkembangan Covid-19 di Kawasan Asia Tenggara', style={'textAlign': 'center', 'color': 'white'}),
                    dcc.Graph(
                    id='tab_baru',
                    figure={
                        'data' : 
                        [
                            {'x' : x_daily, 'y' : y1_daily, 'type' : 'line', 'name' : 'Positif'},
                            {'x' : x_daily, 'y' : y2_daily, 'type' : 'line', 'name' : 'Meninggal'},
                            {'x' : x_daily, 'y' : y3_daily, 'type' : 'line', 'name' : 'Sembuh'}
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
                            {'x' : negara_nama, 'y' : negara_kasus, 'type' : 'bar', 'name' : 'Positif'},
                            {'x' : negara_nama, 'y' : negara_penambahan, 'type' : 'bar', 'name' : '+24 jam Terakhir'}
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
                            {'x' : meninggal_negara_nama, 'y' : meninggal_negara_kasus, 'type' : 'bar', 'name' : 'Positif'},
                            {'x' : meninggal_negara_nama, 'y' : meninggal_negara_penambahan, 'type' : 'bar', 'name' : '+24 jam Terakhir'}
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



