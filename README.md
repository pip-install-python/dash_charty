![Dash Charty](assets/github/example_dash_charty.gif)
# Dash-charty
*still under development*

## Installation

```pip install dash-charty```

## Usage Example

```python 

from dash import *
import dash_charty
import json
from flask import jsonify

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
    html.Div([
          dash_charty.DashCharty(
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
        ) for i in range(6)
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
```

### Data examples located at:
- dash_charty/data/overview_0.json
- dash_charty/data/overview_1.json
- dash_charty/data/overview_2.json
- dash_charty/data/overview_3.json
- dash_charty/data/overview_4.json
- dash_charty/data/overview_5.json

## Supported Props

- id: PropTypes.string,  // The ID of the component
- title: PropTypes.string,  // The title of the chart
- type: PropTypes.string,  // The type of the chart
- data: PropTypes.object,  // The data for the chart
- names: PropTypes.object,  // The names of the data series
- colors: PropTypes.object,  // The colors for the data series
- fillColors: PropTypes.object,  // The fill colors for the data series
- buttonTextColor: PropTypes.object,  // The text color for the buttons
- theme: PropTypes.object,  // The theme for the chart
- animated: PropTypes.bool,  // Whether the chart is animated
- startX: PropTypes.number,  // The start value for the x-axis
- endX: PropTypes.number,  // The end value for the x-axis
- stepX: PropTypes.number,  // The step value for the x-axis
- showLegend: PropTypes.bool,  // Whether to show the legend
- hideFromLegend: PropTypes.object,  // Which data series to hide from the legend
- disabled: PropTypes.object,  // Which data series to disable
- showLegendTitle: PropTypes.bool,  // Whether to show the title in the legend
- legendPosition: PropTypes.string,  // The position of the legend
- showMainArea: PropTypes.bool,  // Whether to show the main area of the chart
- showPreview: PropTypes.bool,  // Whether to show the preview of the chart
- showBrush: PropTypes.bool,  // Whether to show the brush tool
- showButtons: PropTypes.bool,  // Whether to show the buttons
- showRangeText: PropTypes.bool,  // Whether to show the range text
- rangeTextType: PropTypes.string,  // The type of the range text
- xAxisType: PropTypes.string,  // The type of the x-axis
- yAxisType: PropTypes.string,  // The type of the y-axis
- xAxisStep: PropTypes.number,  // The step value for the x-axis
- onZoomIn: PropTypes.func,  // The function to call when zooming in
- zoomInterval: PropTypes.number,  // The interval for zooming in
- zoomStepX: PropTypes.number,  // The step value for zooming in on the x-axis
- autoScale: PropTypes.bool,  // Whether to automatically scale the chart
- minY: PropTypes.number,  // The minimum value for the y-axis
- maxY: PropTypes.number,  // The maximum value for the y-axis
- themes: PropTypes.array,  // The themes for the chart
- themeIdx: PropTypes.number,  // The index of the current theme

## Based on:
- [react-charty](https://99ff00.github.io/react-charty/)

[![Pip Install Python GitHub stats](https://github-readme-stats.vercel.app/api?username=pip-install-python&show_icons=true&theme=radical)](https://github.com/pip-install-python)
