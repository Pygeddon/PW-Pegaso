from django.shortcuts import render
from django.http import HttpResponse
from TicketStore.models import Event
from django.shortcuts import get_object_or_404, redirect
from TicketStore.forms import EventDateUpdateForm
# Create your views here.

def home(request):
    events = Event.objects.all()
    print(events)
    context = {
       'events': events
    }
    return render(request, 'TicketStore/home.html', context)


def event_detail(request, id):
    event = Event.objects.get(event_id=id)
    context = {
        'event': event
    }
    return render(request, 'TicketStore/event_detail.html', context)


def about(request):
    return HttpResponse("<h1>About Us</h1>")


def update_event(request, id):
    event = get_object_or_404(Event, event_id=id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', id=event.event_id)
    else:
        form = EventForm(instance=event)
    
    context = {
        'form': form,
        'event': event
    }
    return render(request, 'TicketStore/update_event.html', context)