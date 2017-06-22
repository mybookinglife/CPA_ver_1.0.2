import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Button, ButtonGroup } from 'react-bootstrap';
import { Link, browserHistory } from 'react-router';
import styles from './record.less';
import cn from 'classnames';
import * as icon from '../../constants/views';
import { deleteBooking } from '../../api/mybookings';
import ModalDialog from '../core/modal-dialog';

class Record extends Component{
    constructor(props) {
        super(props);
    }

    delBooking() {

        deleteBooking(this.props);
    }

    openDialogDelete(){

        $('.bs-modal-delete'+this.props.item.id).modal(this);

    }

    render(){

        const index = this.props.index;
        const cols = this.props.cols;
        const item = this.props.item;

        let title_body = <a>Вы действительно хотите удалить заявку № {item.id} ?</a>;
        let buttons_dialog =
            <div>
                <button type="button" className="btn btn-default" data-dismiss="modal">Cansel
                </button>

                <button type="button" className="btn btn-danger" data-dismiss="modal"
                        onClick={this.delBooking.bind(this)}>Delete
                </button>
            </div>;

        let buttons = (
            <ButtonGroup>
                <Link to={'/mybookings/' + item.id + '/'} className="btn btn-info btn-sm" role="button"><span
                    className={icon.icon_edit}/></Link>
                <ModalDialog className="bs-modal-delete" id={item.id} title={title_body} buttons={buttons_dialog}/>
                <Button bsStyle="danger" bsSize="small" onClick={this.openDialogDelete.bind(this)}><span
                    className={icon.icon_delete}/></Button>
            </ButtonGroup>);


        let new_booking = <span  className={cn({[icon.icon_ok]: item.is_new})}  aria-hidden="true"/>;

        return (
            <tr className={cn({[styles.record]: true})} key={index}>

                {cols.map((col_item, col_index) => {
                    let is_link =  <Link to={'/mybookings/' + item.id + '/'}>{item[col_item.id]}</Link>;
                    return (col_item.is_eval == true) ? <td key={col_index}>{eval(col_item.eval)}</td> : <td key={col_index}>{item[col_item.id]}</td>
                   }
                )}
            </tr>
        );

    };
}

export default Record;