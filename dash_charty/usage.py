from dash import *
import dash_charty
import json
from flask import jsonify
import dash_mantine_components as dmc

app = Dash(__name__)

# Load data from JSON files
data = []
for i in range(6):
    with open(f'data/overview_{i}.json') as f:
        data.append(json.load(f))

data_dict = {i: data[i] for i in range(6)}

themes = [{
    'name': 'dark',
    'grid': { 'color': '#fff', 'alpha': 0.1, 'markerFillColor': '#242f3e' },
    'legend': { 'background': '#1c2533', 'color': '#fff' },
    'preview': { 'maskColor': '#304259', 'maskAlpha': 0.6, 'brushColor': '#56626D', 'brushBorderAlpha': 0, 'handleColor': '#fff' },
    'xAxis': { 'textColor': '#A3B1C2', 'textAlpha': 0.6 },
    'yAxis': { 'textColor': '#A3B1C2', 'textAlpha': 0.6 },
    'title': { 'color': '#fff' },
    'localRange': { 'color': '#fff' },
    'zoomedRange': { 'color': '#fff' },
    'zoomText': { 'color': '#108BE3' },
    'zoomIcon': { 'fill': '#108BE3' },
    'buttons': { 'color': '#fff' },
    'pie': { 'textColor': '#fff' },
    'body': { 'backgroundColor': '#262f3d', 'color': '#fff' },
    'noteColor': '#108BE3',
    'octoColor': '#fff'
  }, {
    'name': 'matrix',
    'grid': { 'color': '#00ff41', 'alpha': 0.2, 'markerFillColor': '#0d0208' },
    'legend': { 'background': '#003b00', 'color': '#00ff41' },
    'preview': { 'maskColor': '#003b00', 'maskAlpha': 0.6, 'brushColor': '#009f11', 'brushBorderAlpha': 0, 'handleColor': '#00ff41' },
    'xAxis': { 'textColor': '#00ff41', 'textAlpha': 0.6 },
    'yAxis': { 'textColor': '#00ff41', 'textAlpha': 0.6 },
    'title': { 'color': '#008f11' },
    'localRange': { 'color': '#008f11' },
    'zoomedRange': { 'color': '#008f11' },
    'zoomText': { 'color': '#008f11' },
    'zoomIcon': { 'fill': '#008f11' },
    'buttons': { 'color': '#0d0208' },
    'pie': { 'textColor': '#0d0208' },
    'colors': {
      'Joined': '#00ff41',
      'Left': '#008f11',
      'Views': '#00ff41',
      'Shares': '#008f11',
      'Clicks': '#008f11',
      'Kiwi': '#00ff41',
      'Apricots': '#008f11',
      'Lemons': '#005b00',
      'Mango': '#7ec251',
      'Oranges': '#145105',
      'Pears': '#66e82f',
      'Apples': '#0acb3b',
      'Adventure': '#03c835',
      'Western': '#008f11',
      'Action': '#00ff41',
      'Multiple Genres': '#66e82f',
      'Drama': '#0acb3b',
      'Comedy': '#008f11',
      'Thriller/Suspense': '#005b00',
      'Concert/Performance': '#7ec251',
      'Horror': '#145105',
      'Romantic Comedy': '#12842f',
      'Musical': '#079d2e'
    }}, {
    'name': 'light',
    'grid': { 'color': '#182D3B', 'alpha': 0.1, 'markerFillColor': '#fff' },
    'legend': { 'background': '#fff', 'color': '#000' },
    'preview': { 'maskColor': '#E2EEF9', 'maskAlpha': 0.6, 'brushColor': '#C0D1E1', 'brushBorderColor': '#fff', 'brushBorderAlpha': 1, 'handleColor': '#fff' },
    'xAxis': { 'textColor': '#8E8E93', 'textAlpha': 1 },
    'yAxis': { 'textColor': '#8E8E93', 'textAlpha': 1 },
    'title': { 'color': '#000' },
    'localRange': { 'color': '#000' },
    'zoomedRange': { 'color': '#000' },
    'zoomText': { 'color': '#108BE3' },
    'zoomIcon': { 'fill': '#108BE3' },
    'buttons': { 'color': '#fff' },
    'pie': { 'textColor': '#fff' },
    'body': { 'backgroundColor': '#fff', 'color': '#000' },
    'noteColor': '#108BE3',
    'octoColor': '#fff'
  }]


app.layout = html.Div([
    html.Button('Switch Theme', id='switch-theme', n_clicks=0),
    dmc.Grid([
          dmc.Col(dash_charty.DashCharty(
            id=f'charty-{i}',
            title=f"Chart {i+1}",
            type=data[i]['type'],
            data=data[i]['data'],
            names=data[i]['names'],
            colors=data[i]['colors'],
            themes=themes,
            rangeTextType='longDate',
            xAxisType='date',
            showMainArea=True,
            showLegend=True,
            animated=True,
            autoScale=True,
            showButtons=True,
            showBrush=True
        ), span=6) for i in range(6)
])])


@app.callback(
    [Output(f'charty-{i}', 'themeIdx') for i in range(6)],  # Update themeIdx prop of each DashCharty
    [Input('switch-theme', 'n_clicks')]
)
def switch_theme(n_clicks):
    return [n_clicks % len(themes)] * 6  # Return new theme index for each DashCharty


@app.server.route('/zoom-in/<date>', methods=['GET'])
def zoom_in(date):
    # Parse the date
    date = int(date)

    # Return the data corresponding to the date
    return jsonify(data_dict[date])

if __name__ == '__main__':
    app.run_server(debug=True, port='3240')