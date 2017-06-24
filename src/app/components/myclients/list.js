import React, {Component, PropTypes} from 'react';
import * as actions from '../../actions/myclients';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

class ListClient extends Component{

    render(){
        return <div></div>
    }

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

export default connect(mapStateToProps, mapDispatchToProps)(ListClient);