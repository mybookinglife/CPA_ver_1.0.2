import { Button } from 'react-bootstrap';
import * as icon from '../../constants/icons';
import store from '../../store';
import * as actions from '../../actions/myclients';
import { addBooking } from '../../api/mybookings';
import { URL_LIST, URL_CLIENTS } from '../../constants/config';

export default function MenuComponent(props){

    const addObject = function () {

        if (this.route.path == URL_LIST) {
            addBooking(this);
        }else if(this.route.path == URL_CLIENTS){
            store.dispatch(actions.addClientSuccess());
        }
    };

    return (
        <div>
            <Button bsStyle="success btn-sm" onClick={addObject.bind(props)} aria-label="Left Align"><span
                className={icon.icon_new}/></Button>
        </div>
    );


}