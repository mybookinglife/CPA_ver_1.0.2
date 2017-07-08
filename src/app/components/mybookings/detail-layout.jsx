import React, {Component, PropTypes} from 'react';
import { Link, browserHistory } from 'react-router';

import ModalDialog from '../core/modal-dialog';
import { editBooking } from '../../api/mybookings';

import LayoutField from './layout-field';

class DetailLayout extends Component{

    constructor(props) {
        super(props);
    }

    closeModal(){
        browserHistory.push('/mybookings/');
    }

    saveChange(){
        this.closeModal();
        editBooking(this.props);

    }

    render(){

        const { id } = this.props.obj;

        let title_body = <a>Заявка № {id}</a>;

        let modal_body = <LayoutField obj={this.props.obj} />;

        let buttons_dialog =
            <div>
                <button type="button" className="btn btn-default" data-dismiss="modal"
                        onClick={this.closeModal}>Close
                </button>

                <button type="button" className="btn btn-primary" data-dismiss="modal"
                        onClick={this.saveChange.bind(this)}>Save changes
                </button>
            </div>

       return (
            <ModalDialog className="bs-modal-detail" size="modal-lg" id={id} title={title_body} body={modal_body} buttons={buttons_dialog}/>

        );

    };
}

export default DetailLayout;