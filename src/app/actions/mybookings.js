import * as types from '../constants/actions';

export function addBookingSuccess(data) {

    return {
        type: types.ADD_BOOKINGS_SUCCESS,
        payload: data
    }

}

export function addBookingError(data) {

    return {
        type: types.ADD_BOOKINGS_ERROR,
        payload: data
    }

}

export function editBookingSuccess(data) {

    return {
        type: types.EDIT_BOOKINGS_SUCCESS,
        payload: data
    }

}

export function editBookingError(data) {

    return {
        type: types.EDIT_BOOKINGS_ERROR,
        payload: data
    }

}

export function deleteBookingSuccess(data) {

    return {
        type: types.DELETE_BOOKINGS_SUCCESS,
        payload: data
    }

}

export function deleteBookingError(data) {

    return {
        type: types.DELETE_BOOKINGS_ERROR,
        payload: data
    }

}

export const getBookingsSuccess = (data) => {
// export function getBookingsSuccess(data) {

    return {
        type: types.GET_BOOKINGS_SUCCESS,
        payload: data
    }

}

export const getBookingsError = (data) => {
// export function getBookingsSuccess(data) {

    return {
        type: types.GET_BOOKINGS_ERROR,
        payload: data
    }

}

export const getProfileBookingSuccess = (data) => {

    return {
        type: types.GET_PROFILE_BOOKINGS_SUCCESS,
        payload: data
    }

}

export const getProfileBookingError = (data) => {

    return {
        type: types.GET_PROFILE_BOOKINGS_ERROR,
        payload: data
    }

}