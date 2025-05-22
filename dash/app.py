from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import plotly.express as px
from dash_bootstrap_components import themes, Card, CardBody

app = Dash(__name__, external_stylesheets=[themes.BOOTSTRAP])

# Загрузка данных
df = pd.read_csv('data/dataset.csv', encoding='latin')

# Обработка пропусков
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Макет дашборда
app.layout = html.Div([
    html.Div([  # Боковая панель
        html.H3("Фильтры"),
        dcc.Dropdown(
            id='year-filter',
            options=[{'label': str(year), 'value': year} for year in df['year'].unique()],
            value=None,
            placeholder="Выберите год"
        ),
    ], style={'width': '20%', 'display': 'inline-block', 'padding': '10px'}),
    html.Div([  # Основной контент
        Card([
            CardBody([
                html.H4("Средний уровень счастья"),
                html.P(id='metric-card')
            ])
        ], style={'margin-bottom': '20px'}),
        dcc.Graph(id='main-graph'),
        dash_table.DataTable(
            id='main-table',
            columns=[
                {'name': 'Country', 'id': 'Country name'},
                {'name': 'Year', 'id': 'year'},
                {'name': 'Happiness Score', 'id': 'Life Ladder'},
                {'name': 'GDP per capita', 'id': 'Log GDP per capita'},
                {'name': 'Social Support', 'id': 'Social support'},
            ],
            page_size=10,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left', 'padding': '5px'},
        ),
        html.Button("Скачать данные", id='download-btn', style={'margin-top': '10px'}),
        dcc.Download(id='download-data')
    ], style={'width': '75%', 'display': 'inline-block', 'float': 'right', 'padding': '10px'})
])

# Callback для обновления графика
@app.callback(
    Output('main-graph', 'figure'),
    Input('year-filter', 'value')
)
def update_graph(selected_year):
    filtered_df = df if selected_year is None else df[df['year'] == selected_year]
    # Столбчатая диаграмма для топ-10 стран по уровню счастья
    if selected_year:
        filtered_df = filtered_df.nlargest(10, 'Life Ladder')  # Топ-10 стран
        title = f'Топ-10 стран по уровню счастья ({selected_year})'
    else:
        title = 'Топ-10 стран по уровню счастья (все годы)'
        filtered_df = filtered_df.groupby('Country name')['Life Ladder'].mean().reset_index().nlargest(10, 'Life Ladder')

    fig = px.bar(filtered_df, x='Country name', y='Life Ladder', title=title,
                 labels={'Life Ladder': 'Уровень счастья', 'Country name': 'Страна'})
    fig.update_layout(xaxis_tickangle=-45)
    return fig

# Callback для обновления таблицы
@app.callback(
    Output('main-table', 'data'),
    Input('year-filter', 'value')
)
def update_table(selected_year):
    filtered_df = df if selected_year is None else df[df['Year'] == selected_year]
    return filtered_df[['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 'Social support']].to_dict('records')

# Callback для карточки
@app.callback(
    Output('metric-card', 'children'),
    Input('year-filter', 'value')
)
def update_card(selected_year):
    filtered_df = df if selected_year is None else df[df['year'] == selected_year]
    mean_happiness = filtered_df['Life Ladder'].mean()
    return f"Средний уровень счастья: {mean_happiness:.2f}"

# Callback для скачивания
@app.callback(
    Output('download-data', 'data'),
    Input('download-btn', 'n_clicks'),
    Input('year-filter', 'value'),
    prevent_initial_call=True
)
def download_data(n_clicks, selected_year):
    filtered_df = df if selected_year is None else df[df['year'] == selected_year]
    return dcc.send_data_frame(filtered_df.to_excel, f"happiness_data_{selected_year or 'all'}.xlsx")

if __name__ == '__main__':
    app.run(debug=True)
