import React, { useContext } from 'react';

import * as AppActions from '../../actions/appActions';

import PropTypes from 'prop-types';

import {AppContext} from "../../contexts/AppContext";

function Navigation(props){
    const {location, history, navigation_items } = props;

    const [app_state, dispatch] = useContext(AppContext);

    return(
        <nav className="navbar navbar-expand-lg navbar-dark fixed-top" id="mainNav">
            <div className="container">
                <a className="navbar-brand js-scroll-trigger" href="#page-top"><img
                    src="assets/img/navbar-logo.svg"/></a>
                <button className="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse"
                        data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false"
                        aria-label="Toggle navigation">Menu<i className="fas fa-bars ml-1"></i></button>
                <div className="collapse navbar-collapse" id="navbarResponsive">
                    <ul className="navbar-nav text-uppercase ml-auto">
                        {
                            navigation_items.map((element, key) =>  <li key={key} className="nav-item" onClick={()=> dispatch({type: AppActions.SET_NAVIGATION_ACTIVE_ITEM, key})}><a className="nav-link js-scroll-trigger">{key}</a></li>)
                        }
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default Navigation
