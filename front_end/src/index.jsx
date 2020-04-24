import React, {useReducer} from "react";
import ReactDom from "react-dom";
import { router } from "./router.jsx";
import app from './reducers/app';
import {initialAppState} from "./reducers/initial_reducer_values/initialAppState";

import * as AppActionTypes from './actions/appActions';

import { AppContext } from './contexts/AppContext';

function App(props) {
  const useReducerReturn = useReducer(app, initialAppState);
  return (
  <AppContext.Provider value={useReducerReturn}>
    {router }
  </AppContext.Provider>
  )
}

ReactDom.render(
    <App/>,
    document.getElementById("app")
);
