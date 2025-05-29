import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_cards(df):
    total_countries = df['Country'].nunique()
    avg_value = df.groupby('Country')['Value'].mean().mean()
    
    cards = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Total de Países", className="card-title"),
                        html.P(f"{total_countries}", id="card-1-value")
                    ])
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Média de Aceitação da Violência", className="card-title"),
                        html.P(f"{avg_value:.2f}%", id="card-2-value")
                    ])
                ])
            ])
        ])
    ])
    return cards

def create_graphs(df):
    country_avg = df.groupby('Country')['Value'].mean().sort_values(ascending=False).head(10)
    
    time_trend = df.groupby('Survey Year')['Value'].mean()
    
    graphs = html.Div([
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='graph-1',
                    figure={
                        'data': [{
                            'x': country_avg.index,
                            'y': country_avg.values,
                            'type': 'bar',
                            'name': 'Média por País'
                        }],
                        'layout': {
                            'title': 'Top 10 Países - Média de Valores',
                            'xaxis': {'tickangle': 45}
                        }
                    }
                )
            ]),
            dbc.Col([
                dcc.Graph(
                    id='graph-2',
                    figure={
                        'data': [{
                            'x': time_trend.index,
                            'y': time_trend.values,
                            'type': 'line',
                            'name': 'Tendência Temporal'
                        }],
                        'layout': {
                            'title': 'Evolução Temporal dos Valores'
                        }
                    }
                )
            ])
        ])
    ])
    return graphs

def create_layout(df):
    layout = dbc.Container([
        html.H1("Estatísticas de violência contra a mulher em escala global", className="text-center my-4"),
        create_cards(df),
        html.Hr(),
        create_graphs(df),
        html.Hr(),
        html.Div([
            html.H4("Filtros", className="text-center"),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='country-filter',
                        options=[{'label': i, 'value': i} for i in sorted(df['Country'].unique())],
                        placeholder="Selecione um país"
                    )
                ])
            ])
        ])
    ], fluid=True)
    return layout