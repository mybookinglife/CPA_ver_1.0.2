import * as types from '../constants/actions';

const initialState = {
  list: [], currentClient: {}

};


function myClients(state = initialState, action) {

    switch (action.type) {
        case types.ADD_CLIENT_ERROR:
            //debugger;
            console.log(action.payload);
            return Object.assign(state);
        default:
            //debugger;
            return Object.assign(state);
    }

}

export default myClients;