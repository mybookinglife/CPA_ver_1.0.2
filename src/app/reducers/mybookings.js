import * as types from '../constants/actions';
import { Link, browserHistory } from 'react-router';

const initialState = {
  list: [], currentBooking: {}

};

function NewUp(a, b) {
    if (a.is_new==true && b.is_new==false) return -1;
    if (a.is_new==false && b.is_new==true) return 1;
}

function myBookings(state = initialState, action) {

    let newlist = {};
    switch (action.type) {
        case types.GET_BOOKINGS_SUCCESS:
            return Object.assign({}, state, {list: action.payload.results.sort(NewUp)});
        case types.GET_BOOKINGS_ERROR:
            console.log(action.payload);
            return Object.assign(state);
        case types.ADD_BOOKINGS_SUCCESS:
            return Object.assign(state);
        case types.ADD_BOOKINGS_ERROR:
            console.log(action.payload);
            return Object.assign(state);
        case types.EDIT_BOOKINGS_SUCCESS:
            return Object.assign({state, list: state.list});
        case types.EDIT_BOOKINGS_ERROR:
            console.log(action.payload);
            return Object.assign(state);
        case types.DELETE_BOOKINGS_SUCCESS:
            newlist = state.list.concat();
            newlist.splice(action.payload, 1);
            return Object.assign({state, list: newlist})
        case types.DELETE_BOOKINGS_ERROR:
            console.log(action.payload);
            return Object.assign(state);
        case types.GET_PROFILE_BOOKINGS_SUCCESS:
            newlist = state.list.concat();
            return Object.assign({state, list: newlist, currentBooking: action.payload})
        case types.GET_PROFILE_BOOKINGS_ERROR:
            console.log(action.payload);
            return Object.assign(state);
        default:
            //debugger;
            return Object.assign(state);
    }

}

export default myBookings;