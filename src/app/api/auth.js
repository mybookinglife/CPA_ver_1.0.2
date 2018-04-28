import {getCookie} from './cookie';
import axios from 'axios';
import {URL, URL_LOGIN, URL_LOGOUT, URL_SERVER,} from "../constants/config"
import {browserHistory} from 'react-router';
import * as ws from './websocket';

export const login = function (username, pass, cb) {
    if (localStorage.token) {
        if (cb) cb(true)
        return
    }
    this.getToken(username, pass, (res) => {
        if (res.authenticated) {

            localStorage.authenticated = res.authenticated
            localStorage.token = res.token
            if (cb) cb(true)
        } else {
            if (cb) cb(false)
        }
    })
};

export const closeSession = function (url) {
    debugger;
    delete localStorage.authenticated;
    delete localStorage.token;
    if (url != undefined) browserHistory.push(url);
};

export const logout = function () {

    let csrftoken = getCookie('csrftoken');


    axios.get(URL_SERVER + '/user/logout/', {

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

        }
    })
        .then(response => {

            if (response.status == 200) {
                closeSession(URL);
                return true;
            }

        })
        .catch(function (error) {
            console.log(error);
            return false;
        });

};

export const loggedIn = function () {

    //debugger;
    return localStorage.authenticated

};

export const getToken = function (username, pass, cb) {

    let csrftoken = getCookie('csrftoken');

    const data = new FormData();
    data.append('username', username);
    data.append('password', pass);

    axios.post(URL_SERVER + '/user/login/', data, {

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }

    })
        .then(response => {
            if (response.status == 200) {
                return cb({
                    authenticated: response.data.result,
                    token: csrftoken
                });
            }
        })
        .catch(function (error) {
            //debugger;
            console.log(error)
        });

};

export const signIn = function (nextState, replace) {

    if (!loggedIn()) {
        replace({
            pathname: URL_LOGIN,
            state: {nextPathname: nextState.location.pathname}
        })
    }else {
        ws.connectWebSocket(this.props);
    }
}


export const signOut = function (nextState, replace) {

     if (logout()) {
         // replace({
         //     pathname: URL,
         //     state: {nextPathname: URL}
         // })
}
}