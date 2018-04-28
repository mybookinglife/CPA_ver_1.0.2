import React, { Component, PropTypes } from 'react';

import Record from './record';
import styles from './list.less';

class ListLayout extends Component{

    render(){

        const { list } = this.props.myBookings;
        const actions = this.props.actions;

        const cols = [
            {id:"id", name: "№", eval: "is_link", is_eval:true},
            {id:"date", name: 'Дата'},
            {id:"time", name: 'Время'},
            {id:"client_name", name: 'Клиент'},
            {id:"phone_client", name: 'Телефон'},
            {id:"service_name", name: 'Услуга'},
            {id:"expert_name", name: 'Специалист',},
            {id:"is_new", name: 'Новая', eval:"new_booking", is_eval: true},
            {id:"actions", name: '', eval:"buttons", is_eval:true}
            ];

        return (
            <table className="table table-hover table-bordered">
                <thead className={styles.list}>
                <tr className={styles.list_thead}>
                    {cols.map((item, index) =>
                        <td>{item.name}</td>
                    )}
                </tr>
                </thead>
                <tbody>
                {list.map((item, index) =>
                    <Record
                        cols={cols}
                        item={item}
                        index={index}
                        actions={actions}
                    />
                )}
                </tbody>
                <tfoot className={styles.list}>
                </tfoot>
            </table>
        );

    };
}

export default ListLayout;
