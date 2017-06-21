import React, { Component } from 'react';

import moment from 'moment';

import 'react-big-calendar/lib/css/react-big-calendar.css';
import BigCalendar from 'react-big-calendar';

BigCalendar.momentLocalizer(moment);

class Calendar extends Component {

render() {

      let events = [
          {
              'title': 'All Day Event',
              'allDay': true,
              'start': new Date(2017, 3, 21),
              'end': new Date(2017, 3, 21)
          },
          {
              'title': 'Long Event',
              'start': new Date(2017, 3, 22),
              'end': new Date(2017, 3, 22)
          },
          {
              'title': 'Meeting',
              'start': new Date(2017, 3, 22, 14, 0, 0, 0),
              'end': new Date(2017, 3, 22, 15, 0, 0, 0)
          },]

    return (

        <div>
            <BigCalendar
                events={events}
            />
        </div>
    );
  }
}

export default Calendar;
