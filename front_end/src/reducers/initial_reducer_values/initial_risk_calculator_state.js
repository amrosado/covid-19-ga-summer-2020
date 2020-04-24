import {List, Map, fromJS } from 'immutable';

export const risk_calculator_initial_state = Map({
    risk_calculator_function: (e) => {
      return (p, i)  => Math.pow(1 - (1 - i / p), e)
    },
   risk_calculator_chart_type: 'line',
   risk_calculator_chart_data:  fromJS({
       labels: ['Dinner Party (10)','Wedding Reception (100)','Small concert (1,000)','Stadium Event(10,000)','Indy 500 (100,000)'],
       datasets: [{
           data: [331494, 33164, 3316, 331, 33],
           label: "1% risk",
           borderColor: "#015D67",
           fill: true
       }, {
           data: [1688344, 169224, 16926, 1692, 169],
           label: "5% risk",
           borderColor: "#00ACB1",
           fill: false
       }, {
           data: [7282186, 735552, 73629, 7363, 736],
           label: "20% risk",
           borderColor: "#87E4DB",
           fill: false
       }, {
           data: [22099112, 2279476, 228659, 22873, 2287],
           label: "50% risk",
           borderColor: "#CAF0C1",
           fill: false
       }
       ]
   }),
    risk_calculator_chart_options: Map({
        title: {
            display: true,
            text: 'Chance that one or more individuals are COVID-19 positive at an event given event size (x-axis) and current case prevalence (y-axis)'
        },
        scales: {
            yAxes: [{
                display: true,
                type: 'logarithmic',
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    })
});
