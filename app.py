import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from components.layout import create_layout
import plotly.express as px
import plotly.graph_objects as go
import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_path, 'src', 'data', 'violence_data.csv')

df = pd.read_csv(data_path)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = create_layout(df)

if __name__ == '__main__':
    app.run(debug=True)