import {List, Map } from 'immutable';

export const initialAppState = Map({
  active_navigation_item: null,
  navigation_items:
  List(
      [
          Map({
            name: "Systems",
            link: "#systems"
          })
      ]
  ),
  scrolledDown: false,
  loggedOn: false,
  topics: [
    {
      name: 'Residency',
      description: 'Generic description'
    },
    {
      name: 'Communication',
      description: 'General description'
    },
    {
      name: 'Academics',
      description: 'General description'
    }
  ]
});

console.log("initial", initialAppState);
