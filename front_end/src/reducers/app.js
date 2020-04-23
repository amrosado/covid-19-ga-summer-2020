import * as AppActionTypes from '../actions/appActions';

export default function app(state, action)  {
  console.log(state);
  switch (action.type) {
    case AppActionTypes.SET_NAVIGATION_ACTIVE_ITEM:
      console.log("State print", state);
      return state.update("active_navigation_item", ()=> action.key)
    default:

      return state;
  }
}