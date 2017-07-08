import React from "react";
import ReactDOM from "react-dom";

import 'bootstrap';
import 'bootstrap/less/bootstrap.less';

import MainMenuLayout from './components/core/main-menu-layout';
import MainComponentLayout from './components/core/main-component-layout';
import Detail from './components/mybookings/detail';
import List from './components/mybookings/list';
import NotFound from './components/core/not-found';
import ListClients from './components/myclients/list';


import Calendar from './components/calendar1';

import { Provider } from 'react-redux';
import store from './store';
import { Router, Route, IndexRoute, hashHistory, browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';


import Login from './components/myusers/login';
import LoginLayout from './components/myusers/login-layout';
import * as auth from './api/auth';
import * as ws from './api/websocket';

const history = syncHistoryWithStore(browserHistory, store);


function login(nextState, replace) {

    if (!auth.loggedIn()) {
        replace({
            pathname:'/login/',
            state: {nextPathname: nextState.location.pathname}
        })
    }else {
        ws.connectWebSocket(this.props);
    }
}

function logout(nextState, replace) {

    if (auth.logout()) {
        // replace({
        //     pathname: '/',
        //     state: {nextPathname: '/'}
        // })
    }
}

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Route path="/" component={MainMenuLayout}>
                <Route onEnter={ login }>
                    <IndexRoute component={Calendar}/>
                    <Route path="mybookings" component={MainComponentLayout}>
                        <IndexRoute component={List}/>
                        <Route path=':id/' component={Detail}/>
                    </Route>
                    <Route path="myclients" component={MainComponentLayout}>
                        <IndexRoute component={ListClients}/>
                        <Route path=':id/' component={Detail}/>
                    </Route>
                    <Route path="mycalendar" component={Calendar}/>
                </Route>
                <Route path='/login/' component={LoginLayout} />
                <Route path='/logout/' onEnter={ logout } />
                <Route path='*' component={NotFound}/>
            </Route>
        </Router>
    </Provider>,
    document.getElementById('mybooking-app')
);