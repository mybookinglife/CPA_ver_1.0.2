import { getBookings } from './mybookings';
import { URL_WebSocket } from '../constants/config';

export function connectWebSocket(props) {
    var webSocket = new WebSocket(URL_WebSocket);
    webSocket.onmessage = function (message) {
        var data = message.data;
        getBookings(props);
    }
}