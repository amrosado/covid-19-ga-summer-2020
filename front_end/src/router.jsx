import React from "react";
import {Router, Route, Switch} from "react-router-dom";
import { createBrowserHistory} from "history";
import styles from './stylesheets/main.scss';

import HomeContainer from "./containers/Home/HomeContainer";

const history = createBrowserHistory();


const router = (
  <Router onUpdate={() => window.scrollTo(0, 0)} history={history}>
    <Switch>
      <Route exact path={"/"} component={HomeContainer}/>
    </Switch>
  </Router>
);

export {router};
