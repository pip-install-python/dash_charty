# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashCharty <- function(id=NULL, animated=NULL, autoScale=NULL, buttonTextColor=NULL, colors=NULL, data=NULL, disabled=NULL, endX=NULL, fillColors=NULL, hideFromLegend=NULL, legendPosition=NULL, maxY=NULL, minY=NULL, names=NULL, onZoomIn=NULL, rangeTextType=NULL, showBrush=NULL, showButtons=NULL, showLegend=NULL, showLegendTitle=NULL, showMainArea=NULL, showPreview=NULL, showRangeText=NULL, startX=NULL, stepX=NULL, theme=NULL, themeIdx=NULL, themes=NULL, title=NULL, type=NULL, xAxisStep=NULL, xAxisType=NULL, yAxisType=NULL, zoomInterval=NULL, zoomStepX=NULL) {
    
    props <- list(id=id, animated=animated, autoScale=autoScale, buttonTextColor=buttonTextColor, colors=colors, data=data, disabled=disabled, endX=endX, fillColors=fillColors, hideFromLegend=hideFromLegend, legendPosition=legendPosition, maxY=maxY, minY=minY, names=names, onZoomIn=onZoomIn, rangeTextType=rangeTextType, showBrush=showBrush, showButtons=showButtons, showLegend=showLegend, showLegendTitle=showLegendTitle, showMainArea=showMainArea, showPreview=showPreview, showRangeText=showRangeText, startX=startX, stepX=stepX, theme=theme, themeIdx=themeIdx, themes=themes, title=title, type=type, xAxisStep=xAxisStep, xAxisType=xAxisType, yAxisType=yAxisType, zoomInterval=zoomInterval, zoomStepX=zoomStepX)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashCharty',
        namespace = 'dash_charty',
        propNames = c('id', 'animated', 'autoScale', 'buttonTextColor', 'colors', 'data', 'disabled', 'endX', 'fillColors', 'hideFromLegend', 'legendPosition', 'maxY', 'minY', 'names', 'onZoomIn', 'rangeTextType', 'showBrush', 'showButtons', 'showLegend', 'showLegendTitle', 'showMainArea', 'showPreview', 'showRangeText', 'startX', 'stepX', 'theme', 'themeIdx', 'themes', 'title', 'type', 'xAxisStep', 'xAxisType', 'yAxisType', 'zoomInterval', 'zoomStepX'),
        package = 'dashCharty'
        )

    structure(component, class = c('dash_component', 'list'))
}
