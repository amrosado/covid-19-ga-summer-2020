import React, { useRef, useLayoutEffect } from 'react';

import PropTypes from 'prop-types';

import ChartJs from 'chart.js';

import ImmutablePropTypes from 'react-immutable-proptypes';

function Chart(props){
    const {chart_data, chart_options, chart_type, intersection_function, chart_dispatch_function } = props;

    const chart_data_js = chart_data.toJS();
    const chart_options_js = chart_options.toJS();

    const chart_ref = useRef(null);

    const event_size_input_ref = useRef(null);

    useLayoutEffect(() => {
        let myChart = new ChartJs(chart_ref.current, {type: chart_type, data: chart_data_js, options: chart_options_js});
    });

    const compute_intersection = (e) => {
        const p = 3000000;
        const i = 100;

        const r = intersection_function(e.target.value)(p, i);

        chart_dispatch_function(parseFloat(e.target.value), i, "example tooltip");
    };

    const chart_style = {
        width: '40em'
    };

    console.log(chart_data_js);

    return(
        <div style={chart_style}>
        <canvas ref={chart_ref} id="myChart" width="400" height="400"/>
        <div>
            <p>Size of the event you're planning on attending:</p>
            <input onChange={(e) => compute_intersection(e)} ref={event_size_input_ref} type="text" placeholder="Event size" id="event_size"/>
        </div>
        </div>
    )
}

Chart.propTypes = {
    chart_data: ImmutablePropTypes.map,
    chart_options: ImmutablePropTypes.map,
    intersection_function: PropTypes.func
}

export default Chart
