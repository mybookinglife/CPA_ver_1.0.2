import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import * as icon from '../../constants/views';
import { addBooking } from '../../api/mybookings';

class Menu extends Component{
   constructor(props) {
        super(props);
    }

     //#TODO Разработать меню с управляющими элементами для списка заявок

    createBooking() {
         addBooking(this.props);
    }

    render(){

        return(
            <div>
                <Button bsStyle="success" onClick={this.createBooking.bind(this)} aria-label="Left Align"><span className={icon.icon_book}/> Создать</Button>
            </div>
        );

    };

}

export default Menu;