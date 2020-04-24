import { Map, List } from 'immutable';

export const initialHomeState = Map({
  summary_items: List(
      [
          Map({
              name: 'Test'
          })
      ]
  ),
  scrolledDown: false,
  loggedOn: false,
})
