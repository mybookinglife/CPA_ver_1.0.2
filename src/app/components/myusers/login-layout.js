import React, {Component, PropTypes} from 'react';
import ModalDialog from '../core/modal-dialog';
import * as auth from '../../api/auth';
import { Form, FormGroup, InputGroup, FormControl, ControlLabel } from 'react-bootstrap';
import {icon_user, icon_lock} from '../../constants/icons';

export default class LoginLayout extends Component{

    constructor(props) {
        super(props);
        this.state = {username:"", password:""};
        this.handleChange = this.handleChange.bind(this);
    };

    componentDidUpdate(){

        // $('.bs-modal-sm-login').modal({backdrop: "static"});
        $('.bs-modal-login').modal();
    };

    handleChange(event){
        this.setState({[event.target.id]: event.target.value});
    };

    handleSubmit() {

        auth.login(this.state.username, this.state.password, (loggedIn) => {
            if (loggedIn) {
                this.context.router.replace(this.props.location.state.nextPathname)
            }
        })
    };

    render() {

        let title_body = <span>Авторизация</span>;

        let modal_body = <form>
            <Form componentClass="fieldset">
               <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon><span className={icon_user}/></InputGroup.Addon>
                        <FormControl id="username" type="text" value={this.state.username} onChange={this.handleChange}/>
                    </InputGroup>
                    </FormGroup>

                    {' '}
                <FormGroup>
                    <InputGroup>
                        <InputGroup.Addon><span className={icon_lock}/></InputGroup.Addon>
                        <FormControl id="password" type="password" value={this.state.password} onChange={this.handleChange}/>
                    </InputGroup>
                </FormGroup>

            </Form>
        </form>;

        let buttons_dialog =
            <div>
                <button type="button" className="btn btn-default" data-dismiss="modal">Close</button>

                <button type="button" className="btn btn-primary" data-dismiss="modal"
                        onClick={this.handleSubmit.bind(this)}>Login
                </button>
            </div>

        return (

            <ModalDialog className="bs-modal-" size="modal-sm" id={'login'} title={title_body} body={modal_body}
                          buttons={buttons_dialog}/>
        )
    }

}

LoginLayout.contextTypes = {
    router: PropTypes.object.isRequired
};