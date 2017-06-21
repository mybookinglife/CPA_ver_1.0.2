import React, { Component } from 'react';
import * as actions from '../actions/mybookings';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import MainComponentLayout from '../components/main-component-layout';
import Menu from '../components/menu';

class Bookings extends Component {

    render() {

        let menu = <Menu actions = {this.props.actions}/>
        return(
            <MainComponentLayout children = {this.props.children} menu = {menu}/>
        );

  };
}

function mapDispatchToProps(dispatch) {

    return {
        actions: bindActionCreators(actions, dispatch)
    }
}

export default connect(mapDispatchToProps)(Bookings);
