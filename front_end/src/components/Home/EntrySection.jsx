import React, { useReducer } from 'react';
import PropTypes from 'prop-types';

function EntrySection(props){
    const {location, history, navigation_items } = props;
    return(
        <section className="masthead">
            <div className="container">
                <div className="masthead-subheading">Welcome To Our Studio!</div>
                <div className="masthead-heading text-uppercase">It's Nice To Meet You</div>
                <a className="btn_custom btn-primary btn-xl text-uppercase js-scroll-trigger" href="#services">Tell Me
                    More</a>
            </div>
        </section>
    )
}

export default EntrySection
