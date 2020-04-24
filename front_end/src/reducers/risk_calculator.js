import { fromJS } from 'immutable';

import * as RiskCalculatorActionTypes from '../actions/risk_calculator_actions';

export default function risk_calculator(state, action)  {
    switch (action.type) {
        case RiskCalculatorActionTypes.UPDATE_RISK_CALCULATOR_CHART:
            return state.update(
                "risk_calculator_chart_data", (chart_data) =>
                    chart_data.update("datasets",
                        (datasets) => datasets.set(4, fromJS({label: "intersection", type: "bubble", data: {x: action.x, y: action.y, r: 10}})) ))
        default:
            return state;
    }
}