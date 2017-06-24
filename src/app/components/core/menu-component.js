import { Button } from 'react-bootstrap';
import * as icon from '../../constants/icons';
import store from '../../store';
import * as actions from '../../actions/myclients';
import { addBooking } from '../../api/mybookings';

export default function MenuComponent(props){

    const addObj = function () {

        if (this.route.path == 'mybookings') {
            addBooking(this);
        }else if(this.route.path == 'myclients'){
            store.dispatch(actions.addClientSuccess());
        }
    };

    return (
        <div>
            <Button bsStyle="success" onClick={addObj.bind(props)} aria-label="Left Align"><span
                className={icon.icon_book}/> Создать</Button>
        </div>
    );


}