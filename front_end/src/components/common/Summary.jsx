import React, { useContext } from 'react';

import ImmutablePropTypes from 'react-immutable-proptypes';

import * as AppActions from '../../actions/appActions';

import PropTypes from 'prop-types';

import {AppContext} from "../../contexts/AppContext";

function Summary(props){
    const {summary_id, summary_name, summary_subheading, summary_items } = props;

    console.log("Summary", summary_items);

    return(
        <section className="page-section" id={summary_id}>
            <div className="text-center">
                <h2 className="section-heading text-uppercase">{summary_name}</h2>
                <h3 className="section-subheading text-muted">{summary_subheading}</h3>
            </div>
            <div className="container">
                {
                    summary_items.map((item, index) =>
                        <div className="col-md-4" key={index}>
                            <span className="fa-stack fa-4x">
                                <i className="fas fa-circle fa-stack-2x text-primary"/>
                                <i className={"fas fa-stack-1x fa-inverse " + item.get('fa_icon')}/>
                            </span>
                        <h4 className="my-3">{item.get('name')}</h4>
                        <p className="text-muted">{item.get('description')}</p>
                    </div>)
                }
            </div>
        </section>
    )
}

Summary.propTypes = {
    summary_items: ImmutablePropTypes.list
}

export default Summary
