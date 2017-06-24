import axios from 'axios';
import * as config from '../constants/config';
import { Link, browserHistory } from 'react-router';
import { getCookie } from './cookie';
import { closeSession } from './auth';
import store from '../store';
import * as actions from '../actions/mybookings';


export function getBookings(props) {

    //const { getBookingsSuccess, getBookingsError } = props.actions;

    let csrftoken = getCookie('csrftoken');
    // let csrftoken = "56073ff4de0ef69c4699c04b1c8d2a8c3efdd5c0";

    return axios.get(config.API_URL + '/mybookings/', {

        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
            // 'Authorization': 'Token ' + csrftoken,

      }
      })
        .then(response => {

            if (response.status == 200) {

                store.dispatch(actions.getBookingsSuccess(response.data))
                //getBookingsSuccess(response.data);
                return response;
            }
        })
        .catch(function (error) {
             // getBookingsError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                browserHistory.push('/mybookings/');
            }
        });
}

export function getProfileBooking(props) {

    const { getProfileBookingSuccess, getProfileBookingError } = props.actions;
    let csrftoken = getCookie('csrftoken');

    return axios.get(config.API_URL + '/mybookings/' + props.id + "/",{

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

      }
      })
        .then(response => {

            if (response.status == 200) {
                getProfileBookingSuccess(response.data);
                return response;
            }

        })
        .catch(function (error) {
            getProfileBookingError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                browserHistory.push('/mybookings/');
            }
        });
}

export function addBooking(props) {

    //const { addBookingSuccess, addBookingError } = props.actions;
    let csrftoken = getCookie('csrftoken');

    let obj = {
        date_time: "2017-03-11T11:00:00Z",
        date: "2017-03-11",
        time: "11:00:00",
        company: 1,
        client: 3,
        service: 1,
        expert: 2,
        note: "Добавляем новую заявку",
        comment: "",
        is_new: true,
        is_cansel: false,
        is_finished: false
    };

    return axios.post(config.API_URL + '/mybookings/create/', obj, {

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

      }
      })
        .then(response => {

            if (response.status == 201) {

                store.dispatch(actions.addBookingSuccess(obj))
                // addBookingSuccess(obj);
                //getBookings(props);
                return response;
            }
        })
        .catch(function (error) {
            store.dispatch(actions.addBookingError(error))
            // addBookingError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                browserHistory.push('/mybookings/');
            }
        });
}


export function editBooking(props) {

    const { editBookingSuccess, editBookingError } = props.actions;
    let csrftoken = getCookie('csrftoken');

    return axios.put(config.API_URL + '/mybookings/' + props.obj.id + "/" + "edit/", props.obj, {

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

      }
      })
        .then(response => {

            if (response.status == 200) {
                editBookingSuccess(props.obj);
                getBookings(props);
                return response;
            }
        })
        .catch(function (error) {
            editBookingError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                getBookings(props);
                browserHistory.push('/mybookings/');
            }
        });
}


export function deleteBooking(props) {

    const { deleteBookingSuccess, deleteBookingError } = props.actions;
    let csrftoken = getCookie('csrftoken');

    return axios.delete(config.API_URL + '/mybookings/' + props.item.id + "/" + "delete/", {

        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

      }
      })
        .then(response => {

            if (response.status == 204) {
                deleteBookingSuccess(props.index);
                return response;
            }
        })
        .catch(function (error) {
            deleteBookingError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                browserHistory.push('/mybookings/');
            }

    });
}

export function getClients() {

    // const { getClientsSuccess, getClientsError } = props.actions;

    return axios.get(config.API_URL + '/mybookings/')
        .then(response => {

            if (response.status == 200) {
                getBookingsSuccess(response.data);
                return response;
            }
        })
        .catch(function (error) {
            getBookingsError(error);
            if (error.response.status == 403 || error.response.status == 401) {
                closeSession();
            } else {
                browserHistory.push('/mybookings/');
            }
        });

}