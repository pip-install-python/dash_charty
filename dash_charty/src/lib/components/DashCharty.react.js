import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Charty from 'react-charty';

class DashCharty extends Component {
    constructor(props) {
        super(props);
        this.state = {
            themeIdx: this.props.themeIdx,
        };

        // this.onZoomIn = this.onZoomIn.bind(this);
    }

    onZoomIn = async (x) => {
        // Convert x to the required format (e.g., date)
        var d = new Date(x),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) month = '0' + month;
        if (day.length < 2) day = '0' + day;

        // Make an HTTP request to the Python endpoint
        var response = await fetch(`/zoom-in/${year}-${month}-${day}`);
        var data = await response.json();

        // Update the state with the new data
        this.setState({ data });
    }

    setTheme = (themeIdx) => {
        if (this.props.themes && themeIdx < this.props.themes.length) {
            var theme = this.props.themes[themeIdx];
            if (theme && theme.body) {
                document.body.style.backgroundColor = theme.body.backgroundColor;
                document.body.style.color = theme.body.color;
            }
        }
    }

    switchTheme = () => {
        var themeIdx = this.state.themeIdx;
        themeIdx++;

        if (themeIdx === this.props.themes.length) {
            themeIdx = 0;
        }

        this.setState({ themeIdx });
        this.setTheme(themeIdx);
    }

    componentDidUpdate(prevProps) {
        if (this.props.themeIdx !== prevProps.themeIdx) {
            this.setState({ themeIdx: this.props.themeIdx });
            this.setTheme(this.props.themeIdx);
        }
    }

    render() {
        const {
            id, title, type, data, names, colors, fillColors, buttonTextColor, theme, animated, startX, endX, stepX,
            showLegend, hideFromLegend, disabled, showLegendTitle, legendPosition, showMainArea, showPreview, showBrush,
            showButtons, showRangeText, rangeTextType, xAxisType, yAxisType, xAxisStep, onZoomIn, zoomInterval, zoomStepX,
            autoScale, minY, maxY, themes, themeIdx, ...otherProps
        } = this.props;

        const currentTheme = themes[this.state.themeIdx];

        return (
            <div id={id}>
                <Charty
                    title={title}
                    theme={currentTheme}
                    type={type}
                    data={data}
                    names={names}
                    colors={colors}
                    fillColors={fillColors}
                    buttonTextColor={buttonTextColor}
                    animated={animated}
                    startX={startX}
                    endX={endX}
                    stepX={stepX}
                    showLegend={showLegend}
                    hideFromLegend={hideFromLegend}
                    disabled={disabled}
                    showLegendTitle={showLegendTitle}
                    legendPosition={legendPosition}
                    showMainArea={showMainArea}
                    showPreview={showPreview}
                    showBrush={showBrush}
                    showButtons={showButtons}
                    showRangeText={showRangeText}
                    rangeTextType={rangeTextType}
                    xAxisType={xAxisType}
                    yAxisType={yAxisType}
                    xAxisStep={xAxisStep}
                    onZoomIn={onZoomIn}
                    zoomInterval={zoomInterval}
                    zoomStepX={zoomStepX}
                    autoScale={autoScale}
                    minY={minY}
                    maxY={maxY}
                    {...otherProps}
                />
            </div>
        );
    }
}

DashCharty.defaultProps = {
    type: 'line',
    data: {},
    names: {},
    colors: {},
    fillColors: {},
    buttonTextColor: {},
    theme: {},
    animated: true,
    startX: undefined,
    endX: undefined,
    stepX: 1,
    showLegend: true,
    hideFromLegend: {},
    disabled: {},
    showLegendTitle: true,
    legendPosition: 'cursor',
    showMainArea: true,
    showPreview: true,
    showBrush: true,
    showButtons: true,
    showRangeText: true,
    rangeTextType: undefined,
    xAxisType: undefined,
    yAxisType: undefined,
    xAxisStep: undefined,
    onZoomIn: undefined,
    zoomInterval: undefined,
    zoomStepX: undefined,
    autoScale: true,
    minY: undefined,
    maxY: undefined,
    themes: [],
    themeIdx: 0,
};

DashCharty.propTypes = {
    id: PropTypes.string,  // The ID of the component
    title: PropTypes.string,  // The title of the chart
    type: PropTypes.string,  // The type of the chart
    data: PropTypes.object,  // The data for the chart
    names: PropTypes.object,  // The names of the data series
    colors: PropTypes.object,  // The colors for the data series
    fillColors: PropTypes.object,  // The fill colors for the data series
    buttonTextColor: PropTypes.object,  // The text color for the buttons
    theme: PropTypes.object,  // The theme for the chart
    animated: PropTypes.bool,  // Whether the chart is animated
    startX: PropTypes.number,  // The start value for the x-axis
    endX: PropTypes.number,  // The end value for the x-axis
    stepX: PropTypes.number,  // The step value for the x-axis
    showLegend: PropTypes.bool,  // Whether to show the legend
    hideFromLegend: PropTypes.object,  // Which data series to hide from the legend
    disabled: PropTypes.object,  // Which data series to disable
    showLegendTitle: PropTypes.bool,  // Whether to show the title in the legend
    legendPosition: PropTypes.string,  // The position of the legend
    showMainArea: PropTypes.bool,  // Whether to show the main area of the chart
    showPreview: PropTypes.bool,  // Whether to show the preview of the chart
    showBrush: PropTypes.bool,  // Whether to show the brush tool
    showButtons: PropTypes.bool,  // Whether to show the buttons
    showRangeText: PropTypes.bool,  // Whether to show the range text
    rangeTextType: PropTypes.string,  // The type of the range text
    xAxisType: PropTypes.string,  // The type of the x-axis
    yAxisType: PropTypes.string,  // The type of the y-axis
    xAxisStep: PropTypes.number,  // The step value for the x-axis
    onZoomIn: PropTypes.func,  // The function to call when zooming in
    zoomInterval: PropTypes.number,  // The interval for zooming in
    zoomStepX: PropTypes.number,  // The step value for zooming in on the x-axis
    autoScale: PropTypes.bool,  // Whether to automatically scale the chart
    minY: PropTypes.number,  // The minimum value for the y-axis
    maxY: PropTypes.number,  // The maximum value for the y-axis
    themes: PropTypes.array,  // The themes for the chart
    themeIdx: PropTypes.number,  // The index of the current theme
};

export default DashCharty;