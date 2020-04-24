import React from 'react';

import {initialAppState} from '../reducers/initial_reducer_values/initialAppState';

export const AppContext = React.createContext(initialAppState);
