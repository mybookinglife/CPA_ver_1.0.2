import * as types from '../constants/actions';

export function addClientSuccess(data) {

    return {
        type: types.ADD_CLIENT_SUCCESS,
        payload: data
    }

}