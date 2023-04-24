# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from utils import showProducts, generateDotsData
from plots.dispersion import Dispersion
from plots.table import Table

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#f2f2f2',
    'text': '#2c2c2c'
}
df = pd.DataFrame(showProducts(72))

# fig1 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig1 = px.bar(df, x="Products", y="Units", color="Name", barmode="group")

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
)


fig1.add_trace(
    px.line(generateDotsData(), x='x_axis', y='y_axis',
            color='colors', title='Some title', color_discrete_sequence=px.colors.sequential.Plasma).data[0]
)


df = px.data.election()

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),


    html.P(children='Selling Rate per Article', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.P(children='[Last Month]', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig1
    ),


    html.Div(className="quarter", children=[
        Dispersion(app),

    ]),
    html.Div(children=[
        Table(),
    ])

    # dcc.Graph(
    #     id='Mapa Montreal',
    #     figure=fig
    # )
])


# fig.show()

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
