import React, {Component} from 'react';
import {connect} from 'react-redux';

import {bindActionCreators} from 'redux';
import * as actions from '../actions/mybookings';
import NotFound from '../components/not-found'
import DetailLayout from '../components/detail'
import ListLayout from '../components/list';
import * as Api from '../api/mybookings';


class Detail extends Component {

    componentDidMount() {
        Api.getProfileBooking(this.props);
    }

    componentDidUpdate() {

        //noinspection JSCheckFunctionSignatures
        $('.bs-modal-detail' + this.props.id).modal({backdrop: "static"});

    }

    render() {

        const actions = this.props.actions;
        const currentBooking = this.props.myBookings.currentBooking;

        let response = <NotFound />;
        if (currentBooking != undefined && currentBooking.id == this.props.id) {
            response =
                <div>
                    <ListLayout
                        myBookings={this.props.myBookings}
                        actions={this.props.actions}
                    />
                    <DetailLayout obj={currentBooking} actions={actions}/>
                </div>
        } else {
            response =
                <div>
                    <ListLayout
                        myBookings={this.props.myBookings}
                        actions={this.props.actions}
                    />
                </div>
        }

        return (response);

    };
}

function mapStateToProps(state, ownProps) {

    return {
        myBookings: state.myBookings,
        id: Number(ownProps.routeParams.id),
        ownProps
    }
}

function mapDispatchToProps(dispatch) {

    return {
        actions: bindActionCreators(actions, dispatch)
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Detail);