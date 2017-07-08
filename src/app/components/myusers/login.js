import React, { Component } from 'react';
import LoginLayout from './login-layout';


export default class Login extends Component{

    constructor(props){
        super(props);
    };

    componentDidUpdate() {

        $('.bs-modal-login').modal({backdrop: "static"});

    }
    render() {
        return (
            <LoginLayout />
          )
    };
}
