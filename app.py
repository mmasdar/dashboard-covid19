import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from assets import global_tab, asia_tenggara_tab, indonesia_tab

import pandas as pd
import plotly.figure_factory as ff
import numpy as np

import plotly.graph_objs as go
import datetime

# get data directly from github. The data source provided by Johns Hopkins University.
url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_deaths = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_recovered = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

df_confirmed = pd.read_csv(url_confirmed)
df_deaths = pd.read_csv(url_deaths)
df_recovered = pd.read_csv(url_recovered)

def datatime_convert(date_str,days_to_add=0):

    format_str = '%m/%d/%y' # The format
    datetime_obj = datetime.datetime.strptime(date_str, format_str)
    datetime_obj += datetime.timedelta(days=days_to_add)
    return datetime_obj.strftime('%d-%b-%Y')

external_stylesheets = ["static/css/style.css", 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {"background": "#2D2D2D", "background_div": "white", 'text': 'white'}

app.config['suppress_callback_exceptions']= True

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('DASHBOARD DATA Covid-19', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    html.Div([html.Span('Data diupdate secara otomatis dari Database John Hopkins University. Terakhir diupdate pada: ',
                             style={'color': colors['text'],
                             }),
            html.Span(datatime_convert(df_confirmed.columns[-1],1) + '  00:01 (UTC).',
                             style={'color': '#2d67e0',
                             'fontWeight': 'bold',
                             }),
                        ], style={'textAlign' : 'center'}),


    dcc.Tabs(id="tabs", className="row", style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='med_tab', children=[
        dcc.Tab(label='Global', value='data'),
        dcc.Tab(label='Asia Tenggara', value='dem_tab'),
        dcc.Tab(label='Indonesia', value='med_tab')
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])


def render_content(tab):
    if tab == 'dem_tab'     :
        return asia_tenggara_tab.tab_3_layout
    elif tab == 'med_tab'   :
        return indonesia_tab.tab_3_layout
    elif tab == 'data'      :
        return global_tab.tab_3_layout


if __name__ == "__main__":
    app.run_server(debug=True)