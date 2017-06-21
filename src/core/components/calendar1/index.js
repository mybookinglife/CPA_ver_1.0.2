import React, { Component } from 'react';

import $ from 'jquery';
import 'moment';

import 'fullcalendar/dist/fullcalendar.js';
import 'fullcalendar/dist/fullcalendar.min.css';

class AppCalendar extends Component {

  componentDidMount(){
    const { calendar } = this.refs;

    $(calendar).fullCalendar({
            theme: true,
			header: {
				left: 'prev,next, today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay,listMonth'
			},
			defaultDate: '2017-04-10',
			navLinks: true, // can click day/week names to navigate views
			editable: true,
			eventLimit: true, // allow "more" link when too many events
			events: this.props.events,
			eventAllow: function(dropLocation, draggedEvent) {
			    if (draggedEvent.id === 1) {
			        return false
			    }
			    else {
			        return true;
			    }
			},
		    eventResize: function(event, delta, revertFunc) {

		        alert(event.title + " end is now " + event.end.format());

		        if (!confirm("is this okay?")) {
		            revertFunc();
		        }

		    }

    });
  }

  render() {
    return (
      <div ref='calendar'></div>
    );
  }

}


class Calendar extends Component {
  render() {

    let events = [
      {
          id: 1,
          title: 'Задача 1',
          start: '2017-04-21T09:00:00',
          end: '2017-04-21T10:00:00',
      },
      {
          id: 2,
          title: 'Задача 2',
          start: '2017-04-22T16:00:00',
          end: '2017-04-22T17:00:00',
      },
      {
          id: 3,
          title: 'Задача 3',
          start: '2017-04-23',
          end: '2017-04-23',
      },

    ]

    return (
      <div className="App">
        <AppCalendar events={events} />
      </div>
    );
  }
}

export default Calendar;