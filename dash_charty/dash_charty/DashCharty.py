# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCharty(Component):
    """A DashCharty component.


Keyword arguments:

- id (string; optional)

- animated (boolean; default True)

- autoScale (boolean; default True)

- buttonTextColor (dict; optional)

- colors (dict; optional)

- data (dict; optional)

- disabled (dict; optional)

- endX (number; default undefined)

- fillColors (dict; optional)

- hideFromLegend (dict; optional)

- legendPosition (string; default 'cursor')

- maxY (number; default undefined)

- minY (number; default undefined)

- names (dict; optional)

- rangeTextType (string; default undefined)

- showBrush (boolean; default True)

- showButtons (boolean; default True)

- showLegend (boolean; default True)

- showLegendTitle (boolean; default True)

- showMainArea (boolean; default True)

- showPreview (boolean; default True)

- showRangeText (boolean; default True)

- startX (number; default undefined)

- stepX (number; default 1)

- theme (dict; optional)

- themeIdx (number; default 0)

- themes (list; optional)

- title (string; optional)

- type (string; default 'line')

- xAxisStep (number; default undefined)

- xAxisType (string; default undefined)

- yAxisType (string; default undefined)

- zoomInterval (number; default undefined)

- zoomStepX (number; default undefined)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_charty'
    _type = 'DashCharty'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, title=Component.UNDEFINED, type=Component.UNDEFINED, data=Component.UNDEFINED, names=Component.UNDEFINED, colors=Component.UNDEFINED, fillColors=Component.UNDEFINED, buttonTextColor=Component.UNDEFINED, theme=Component.UNDEFINED, animated=Component.UNDEFINED, startX=Component.UNDEFINED, endX=Component.UNDEFINED, stepX=Component.UNDEFINED, showLegend=Component.UNDEFINED, hideFromLegend=Component.UNDEFINED, disabled=Component.UNDEFINED, showLegendTitle=Component.UNDEFINED, legendPosition=Component.UNDEFINED, showMainArea=Component.UNDEFINED, showPreview=Component.UNDEFINED, showBrush=Component.UNDEFINED, showButtons=Component.UNDEFINED, showRangeText=Component.UNDEFINED, rangeTextType=Component.UNDEFINED, xAxisType=Component.UNDEFINED, yAxisType=Component.UNDEFINED, xAxisStep=Component.UNDEFINED, onZoomIn=Component.UNDEFINED, zoomInterval=Component.UNDEFINED, zoomStepX=Component.UNDEFINED, autoScale=Component.UNDEFINED, minY=Component.UNDEFINED, maxY=Component.UNDEFINED, themes=Component.UNDEFINED, themeIdx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animated', 'autoScale', 'buttonTextColor', 'colors', 'data', 'disabled', 'endX', 'fillColors', 'hideFromLegend', 'legendPosition', 'maxY', 'minY', 'names', 'rangeTextType', 'showBrush', 'showButtons', 'showLegend', 'showLegendTitle', 'showMainArea', 'showPreview', 'showRangeText', 'startX', 'stepX', 'theme', 'themeIdx', 'themes', 'title', 'type', 'xAxisStep', 'xAxisType', 'yAxisType', 'zoomInterval', 'zoomStepX']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animated', 'autoScale', 'buttonTextColor', 'colors', 'data', 'disabled', 'endX', 'fillColors', 'hideFromLegend', 'legendPosition', 'maxY', 'minY', 'names', 'rangeTextType', 'showBrush', 'showButtons', 'showLegend', 'showLegendTitle', 'showMainArea', 'showPreview', 'showRangeText', 'startX', 'stepX', 'theme', 'themeIdx', 'themes', 'title', 'type', 'xAxisStep', 'xAxisType', 'yAxisType', 'zoomInterval', 'zoomStepX']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashCharty, self).__init__(**args)
