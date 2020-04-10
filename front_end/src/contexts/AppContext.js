import React from 'react';

import {initialAppState} from '../reducers/initialReducerValues/initialAppState';

export const AppContext = React.createContext(initialAppState);
