import React, { useReducer, useContext } from 'react';
import PropTypes from 'prop-types';

import { HomeContext } from '../../contexts/HomeContext';

import Home from '../../components/Home/Home';

import home from '../../reducers/home';

import {initialHomeState} from "../../reducers/initial_reducer_values/initialHomeState";

import { AppContext } from '../../contexts/AppContext';

function HomeContainer(props){
  const {location, history } = props;

  const [app_state, dispatch] = useContext(AppContext);
  
  const navigation_items = app_state.get('navigation_items');
  
  return(
    <HomeContext.Provider value={useReducer(home, initialHomeState)}>
 {/*     <Home navigation_items={navigation_items}/>*/}
    </HomeContext.Provider>
  )
}

export default HomeContainer
