import React, { useContext } from 'react';

import ImmutablePropTypes from 'react-immutable-proptypes';

function Research(props){
    const {research_id, research_name, research_subheading, research_items } = props;

    return(
        <section className="page-section bg-light" id={research_id}>
            <div className="container">
                <div className="text-center">
                    <h2 className="section-heading text-uppercase">{research_name}</h2>
                    <h3 className="section-subheading text-muted">{research_subheading}</h3>
                </div>
                <div className="row">
                    {
                        research_items.map(
                            (item, index) =>
                                <div className="col-lg-4 col-sm-6 mb-4">
                                <div className="portfolio-item">
                                    <a className="portfolio-link" data-toggle="modal" href="#portfolioModal1">
                                        <div className="portfolio-hover">
                                            <div className="portfolio-hover-content"><i className="fas fa-plus fa-3x"></i>
                                            </div>
                                        </div>
                                        <img className="img-fluid" src="assets/img/portfolio/01-thumbnail.jpg" alt=""
                                        /></a>
                                    <div className="portfolio-caption">
                                        <div className="portfolio-caption-heading">{item.get('name')}</div>
                                        <div className="portfolio-caption-subheading text-muted">{item.get('description')}</div>
                                    </div>
                                </div>
                            </div>
                        )
                    }
                </div>
            </div>
        </section>
    )
};

Research.propTypes = {
    research_items: ImmutablePropTypes.list
};

export default Research;
