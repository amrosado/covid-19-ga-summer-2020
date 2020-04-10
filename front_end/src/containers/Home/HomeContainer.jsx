import React, { useReducer } from 'react';
import PropTypes from 'prop-types';

import { HomeContext } from '../../contexts/HomeContext';

import home from '../../reducers/home';

import {initialHomeState} from "../../reducers/initialReducerValues/initialHomeState";

function HomeContainer(props){
  const {location, history } = props;
  return(
    <HomeContext.Provider value={useReducer(home, initialHomeState)}>
    </HomeContext.Provider>
  )
}

export default HomeContainer
