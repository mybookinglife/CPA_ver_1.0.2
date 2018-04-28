import { combineReducers } from 'redux';
import { routerReducer} from 'react-router-redux';


import myClients from './myclients';
import myBookings from './mybookings';

const rootReducer = combineReducers({
    routing: routerReducer,
    myBookings,
    myClients,
});

export default rootReducer;