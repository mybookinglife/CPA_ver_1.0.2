import { combineReducers } from 'redux';
import { routerReducer} from 'react-router-redux';

import myBookings from './mybookings';


const rootReducer = combineReducers({
    routing: routerReducer,
    myBookings,
});

export default rootReducer;