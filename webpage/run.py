import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

#Loading the Dataframe from the Project folder
df = pd.read_csv('../new_coviddataset.csv')
#Generation of the Options for the Dropdown Menu
dropdown_option = [{"label":country, "value":country} for country in df['location'].unique()]

#Initialization of the App
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP,"https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"])

app.layout = dbc.Container(
    fluid=True,
    style={'backgroundColor': '#e9ecef'},
    children=[
      dbc.NavbarBrand(
                    html.Img(
                        src="https://www.nursingworld.org/~4987f1/contentassets/100e612c71cd4178a7bebb584ed3bb48/covid19-resource-center-logo-gray.png",
                        height="90px",
                        className="mx-auto d-block"
                    ),
                    className="navbar-brand-centered",
                    href="#"
                    
                ),
        dbc.Container(
            fluid=True,
            children=[
                dbc.Row(
                    dbc.Col(
                        html.H1("Covid-19 Cases and Vaccine Impact", className="text-center mt-4", style={'font-weight': 'bold'})
                    )
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H5("The COVID-19 Epidemic", className="card-title"),
                                            html.P(
                                                "The COVID-19 epidemic has had a significant global impact, spreading rapidly and causing widespread disruption. The virus, known as SARS-CoV-2, is primarily transmitted through respiratory droplets and can cause a range of symptoms from mild to severe. Governments and health organizations have implemented measures like social distancing and mask mandates to slow the spread. The pandemic has brought economic challenges and changed the way people live and interact. Efforts continue to combat the epidemic through research, cooperation, and public health interventions.",
                                                className="card-text"
                                            )
                                        ]
                                    )
                                ],
                                className="mb-4 animate__animated animate__fadeIn"
                            )
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4('Cases before and after vaccination'),
                                #Dropdown Menu for the choosing of the Country
                                dcc.Dropdown(
                                    id="dropdown",
                                    options=dropdown_option,
                                    value='Afghanistan'
                                ),
                                html.Div(id='graph_container')
                            ],
                            width={"size": 4}
                        ),
                        dbc.Col(
                            #Checklist for the choosing of the Requested Data
                            dcc.Checklist(
                                id="checklist",
                                options=[
                                    {'label': 'Total Cases', 'value': 'total_cases'},
                                    {'label': 'Total Deaths', 'value': 'total_deaths'},
                                    {'label': 'Population', 'value': 'population'},
                                    {'label': 'Fully Vacinations', 'value': 'people_fully_vaccinated'},
                                    {'label': 'Total Cases per Million', 'value': 'total_cases_per_million'},
                                    {'label': 'Total deaths per Million', 'value': 'total_deaths_per_million'}
                                ],
                                value=['total_cases'],
                                inline=False
                            ),
                            width={"size": 4, "offset": 4}
                        )
                    ],
                    className="mt-4 animate__animated animate__fadeIn"
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Graph(id="graph"),
                            width={"size": 8, "offset" : 2}
                        )
                    ],
                    className="animate__animated animate__fadeInleft"
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("The Global COVID-19 Epidemic", className="card-title"),
                                        html.P(
                                            "The graph depicts the global COVID-19 epidemic, illustrating the cumulative number of cases, COVID-related deaths, and vaccination rates over time. It offers valuable insights into the scale of the virus's spread, the devastating impact of fatalities, and the progress made in administering vaccines worldwide. This visual representation enablesyou to understand the interconnectedness of these variables and informs public health strategies to combat the pandemic effectively.",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="mb-4 animate__animated animate__fadeIn"
                        )
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("Authors", className="card-title"),
                                         html.Img(
                                            src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/HNU-Logo.svg/1200px-HNU-Logo.svg.png",
                                            alt="Author Image",
                                            className="card-img",
                                            style={'max-width': '10%', 'height': 'auto'}
                                        ),
                                        
                                        html.P(
                                            "Alexander Schaefer | Dino Azizovic | Shaheer Waqar | HNU SS23",
                                            className="card-text"
                                        )
                                    ]
                                )
                            ],
                            className="mb-4 animate__animated animate__fadeIn"
                        )
                    )
                )
            ]
        )
    ]
)

@app.callback(
   #Callback option to generate the Values from the Checkboxes and Dropdown Menu
    Output("graph", "figure"),
    Input("dropdown", "value"),
    Input("checklist", "value")
)
# Generation of the Chart with Multiple Lines in the Graph
def update_line_chart(country, selected_dataset):
    #Editing of the DataFrame to request only the choosen Country
    df_edit = df.query(f"location == '{country}'")

    traces = []

    # Creation of all the "lines" choosen based on the Datapoints in the Checkboxes
    for dataset in selected_dataset:
        trace = go.Scatter(
            x=df_edit['date'],
            y=df_edit[dataset],
            mode='lines',
            name=dataset
        )
        traces.append(trace)

    # Creation of the Layout
    layout = go.Layout(
        title = f'Dataset of {country}',
        xaxis={'title': 'Date'},
        yaxis={'title': 'Datasets'}
    )
    # Making of the Figure with the different lines
    fig = go.Figure(data=traces, layout=layout)

    # Returning the figure to Output "graph"
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
