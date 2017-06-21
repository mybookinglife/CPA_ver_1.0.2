
import json
from django.http import HttpResponse
# from django.template.context_processors import csrf
from django.shortcuts import render
from mybookings.api.views import BookingListApiView

# Create your views here.
def get_events(request):
    
    if request.method == 'POST':

        response_data = {}
#         response_data.update(csrf(request))
        
        response_data = [{'id': 999,'title': 'All Day Event',
                    'start': '2016-09-01T15:00:00',
                    'end': '2016-09-01T17:00:00', 'overlap': False,},{'id': 10,'title': 'Task 2',
                    'start': '2016-09-01T16:00:00','overlap': False,
                },]

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
            )
    
    else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )

        response_data = {}
#         response_data.update(csrf(request))
        
        response_data = {}
        
        
        response_data = [{'id': 999, 'title': 'All Day Event',
                    'start': '2016-09-01'
                },]

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
            )


def show_calendar(request):
    
    response_data = {}
#     response_data.update(csrf(request))

    result_rest = HttpResponse(BookingListApiView.as_view())

    # Group('chat').send({'text': json.dumps({'message': 'Сообщение создано автоматически',
    #                                         'sender': 'Календарь'})})

    return HttpResponse(
        render(request, 'main.html', response_data))
