import React, {Component, PropTypes} from 'react';
import * as actions from '../actions/mybookings';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

import * as Api from '../api/mybookings';

import ListLayout from '../components/list';

class List extends Component {

    constructor(props) {
        super(props);

    }

    componentDidMount() {

        Api.getBookings(this.props);

    }

    render() {

        console.log(this.props);
        // debugger;

        return (
            <div>
                <ListLayout
                    myBookings={this.props.myBookings}
                    actions={this.props.actions}
                />
            </div>
        );
    };

}

function mapStateToProps(state, ownProps) {

    return {
        myBookings: state.myBookings,
        ownProps
    }
}

function mapDispatchToProps(dispatch) {

    return {
        actions: bindActionCreators(actions, dispatch)
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(List);
