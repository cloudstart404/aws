import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Initialize the app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# App Layout
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Cloud Start 🌩️",
                        style={
                            "textAlign": "center",
                            "fontSize": "5rem",
                            "color": "#00CED1",
                            "marginTop": "50px",
                        }),
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col(
                html.H3("Your Journey to Cloud & Data Begins Here",
                        style={
                            "textAlign": "center",
                            "fontSize": "2rem",
                            "color": "#FFD700",
                        }),
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col(
                html.P("Learn AWS, Azure, Docker, Terraform, Python, SQL, Power BI",
                       style={
                           "textAlign": "center",
                           "fontSize": "1.5rem",
                           "color": "#FFFFFF",
                           "marginTop": "20px",
                       }),
                width=12,
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    dcc.Loading(
                        type="circle",
                        children=html.Div(id="loading-output"),
                        color="#00CED1"
                    ),
                    style={"textAlign": "center", "marginTop": "50px"}
                ),
                width=12
            )
        )
    ],
    fluid=True,
    style={"backgroundColor": "#1E1E1E", "height": "100vh"}
)

# Run the app
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)