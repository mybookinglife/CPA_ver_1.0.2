import { getCookie } from './cookie';
import axios from 'axios';
import * as config from '../constants/config';
import { browserHistory } from 'react-router';

module.exports = {
    login: function(username, pass, cb) {
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
    },

    closeSession: function () {
        //debugger;
        delete localStorage.authenticated;
        delete localStorage.token;
        browserHistory.push('/login/');
    },

    logout: function() {

        let csrftoken = getCookie('csrftoken');


        axios.get(config.URL + '/user/logout/', {

            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,

            }
        })
            .then(response => {

                //debugger;
                if (response.status == 200) {
                    delete localStorage.authenticated;
                    delete localStorage.token;
                    return true;
                }

            })
            .catch(function (error) {
                console.log(error);
                return false;
            });

    },

    loggedIn: function() {

        //debugger;
        return localStorage.authenticated

    },

    getToken: function(username, pass, cb) {

        let csrftoken = getCookie('csrftoken');

        const data = new FormData();
        data.append('username', username);
        data.append('password', pass);

        axios.post(config.URL + '/user/login/', data, {

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

    },
}