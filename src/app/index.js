import React from "react";
import ReactDOM from "react-dom";

import 'bootstrap';
import 'bootstrap/less/bootstrap.less';

import MainMenuLayout from './components/core/main-menu-layout';
import MainComponentLayout from './components/core/main-component-layout';
import CommonLayout from './components/core/common-layout';


import Detail from './components/mybookings/detail';
import List from './components/mybookings/list';
import NotFound from './components/core/not-found';
import ListClients from './components/myclients/list';

import {URL_LOGIN, URL_LOGOUT, URL_CALENDAR, URL_CLIENTS, URL_LIST, URL} from './constants/config';


import Calendar from './components/calendar1';

import { Provider } from 'react-redux';
import store from './store';
import { Router, Route, IndexRoute, hashHistory, browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';

import Login from './components/myusers/login';
import {signIn, signOut} from "./api/auth";
const history = syncHistoryWithStore(browserHistory, store);

const pushMain = function () {
    browserHistory.push(URL);
}

ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Route path={URL}>
                <IndexRoute component={CommonLayout}/>
                <Route component={MainMenuLayout} onEnter={ signIn } >
                    <Route path={URL_LIST} component={MainComponentLayout}>
                        <IndexRoute component={List}/>
                        <Route path=':id/' component={Detail}/>
                    </Route>
                    <Route path={URL_CLIENTS} component={MainComponentLayout}>
                        <IndexRoute component={ListClients}/>
                        <Route path=':id/' component={Detail}/>
                    </Route>
                    <Route path={URL_CALENDAR} component={Calendar}/>
                </Route>
                <Route path = {URL_LOGIN} component={Login} />
                <Route path = {URL_LOGOUT} onEnter={ signOut } />
                <Route path='/index/' onEnter={ pushMain }/>
                <Route path='*' component={NotFound}/>
            </Route>
        </Router>
    </Provider>,
    document.getElementById('mybooking-app')
);