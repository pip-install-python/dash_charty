# AUTO GENERATED FILE - DO NOT EDIT

export dashcharty

"""
    dashcharty(;kwargs...)

A DashCharty component.

Keyword arguments:
- `id` (String; optional)
- `animated` (Bool; optional)
- `autoScale` (Bool; optional)
- `buttonTextColor` (Dict; optional)
- `colors` (Dict; optional)
- `data` (Dict; optional)
- `disabled` (Dict; optional)
- `endX` (Real; optional)
- `fillColors` (Dict; optional)
- `hideFromLegend` (Dict; optional)
- `legendPosition` (String; optional)
- `maxY` (Real; optional)
- `minY` (Real; optional)
- `names` (Dict; optional)
- `rangeTextType` (String; optional)
- `showBrush` (Bool; optional)
- `showButtons` (Bool; optional)
- `showLegend` (Bool; optional)
- `showLegendTitle` (Bool; optional)
- `showMainArea` (Bool; optional)
- `showPreview` (Bool; optional)
- `showRangeText` (Bool; optional)
- `startX` (Real; optional)
- `stepX` (Real; optional)
- `theme` (Dict; optional)
- `themeIdx` (Real; optional)
- `themes` (Array; optional)
- `title` (String; optional)
- `type` (String; optional)
- `xAxisStep` (Real; optional)
- `xAxisType` (String; optional)
- `yAxisType` (String; optional)
- `zoomInterval` (Real; optional)
- `zoomStepX` (Real; optional)
"""
function dashcharty(; kwargs...)
        available_props = Symbol[:id, :animated, :autoScale, :buttonTextColor, :colors, :data, :disabled, :endX, :fillColors, :hideFromLegend, :legendPosition, :maxY, :minY, :names, :rangeTextType, :showBrush, :showButtons, :showLegend, :showLegendTitle, :showMainArea, :showPreview, :showRangeText, :startX, :stepX, :theme, :themeIdx, :themes, :title, :type, :xAxisStep, :xAxisType, :yAxisType, :zoomInterval, :zoomStepX]
        wild_props = Symbol[]
        return Component("dashcharty", "DashCharty", "dash_charty", available_props, wild_props; kwargs...)
end

