import React, { useReducer, useContext } from 'react';

import PropTypes from 'prop-types';

import Chart from '../../components/common/Chart';

import * as RiskCalculatorActions from '../../actions/risk_calculator_actions';

import risk_calculator from '../../reducers/risk_calculator';

import {risk_calculator_initial_state} from "../../reducers/initial_reducer_values/initial_risk_calculator_state";

import { RiskCalculatorContext } from '../../contexts/RiskCalculatorContext';

function RiskCalculatorContainer(props){
    const {location, history } = props;

    const use_reducer_output = useReducer(risk_calculator, risk_calculator_initial_state);

    const [risk_calculator_state, risk_calculator_dispatch ] = use_reducer_output;

    const risk_calculator_dispatch_function = (x, y, tooltip) => {
        console.log("intersection", x, y);
        risk_calculator_dispatch({type: RiskCalculatorActions.UPDATE_RISK_CALCULATOR_CHART, x: x,y: y, tooltip})
    };

    const risk_calculator_chart_data = risk_calculator_state.get('risk_calculator_chart_data');

    const risk_calculator_chart_options = risk_calculator_state.get('risk_calculator_chart_options');

    const risk_calculator_chart_type = risk_calculator_state.get('risk_calculator_chart_type');

    const risk_calculator_function = risk_calculator_state.get('risk_calculator_function');

    return(
        <RiskCalculatorContext.Provider value={use_reducer_output}>
            <Chart chart_dispatch_function={risk_calculator_dispatch_function} intersection_function={risk_calculator_function}  chart_data={risk_calculator_chart_data} chart_options={risk_calculator_chart_options} chart_type={risk_calculator_chart_type}/>
        </RiskCalculatorContext.Provider>
    )
}

export default RiskCalculatorContainer
