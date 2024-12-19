from django.shortcuts import render
from django.http import HttpResponse
from TicketStore.models import Event
from django.shortcuts import get_object_or_404, redirect
from TicketStore.forms import EventDateUpdateForm
import datetime


# Creo le viste per la home e per la pagina di dettaglio dell'evento

def home(request):
    
    #Recupero tutti gli eventi presenti nel db
    events = Event.objects.all()
    
    #Controllo l'output
    print(events)
    
    #invio il contesto al template home.html
    context = {
       'events': events
    }
    return render(request, 'TicketStore/home.html', context)


def event_detail(request, id):
    
    #Ottengo l'evento con l'id passato come parametro recuperando l'evento associato alla id
    event = Event.objects.get(event_id=id)
    
    #Ottengo tutte le date associate all'evento
    dates = event.event_date.all()
    
    #controllo l'output
    print(event)
    
    #Essendo le date in realtà un range tra data inizio evento e data fine evento, creo un array di date
    #che comprenderà tutte le date intermedie compresi ovviamente gli estremi
    
    #creo l'array vuoto
    date_ranges = []
    
    #Per ogni data presente nel range, aggiungo le date intermedie all'array con append()
    for date in dates:
        current_date = date.date_from
        while current_date <= date.date_to:
            date_ranges.append(current_date)
            
            #utilizzo la funzione timedelta per incrementare la data di un giorno
            current_date += datetime.timedelta(days=1)
            
    #Controllo l'output
    for date in date_ranges:
        print(date)
        
    #Creo il contesto da passare al template integrando sia l'evento che le date intermedie    
    context = {
        'event': event,
        'dates': date_ranges,
    }
    return render(request, 'TicketStore/event_detail.html', context)


#Creo la vista per la pagina about che non svilupperò poiche non utile per i nostri fini. serve piu
#che altro per riempire il menu di navigazione
def about(request):
    return HttpResponse("<h1>About Us</h1>")


#crea una vista per procedere con l'acquisto del biglietto. la data dell'evento sarà passata come
#parametro insieme all'id dell'evento.

def buy_ticket(request, id, date):
    event = Event.objects.get(event_id=id)
    context = {
        'event': event,
        'date': date,
    }
    return render(request, 'TicketStore/buyourticket.html', context)





# def update_event(request, id):
#     event = get_object_or_404(Event, event_id=id)
#     if request.method == 'POST':
#         form = EventForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('event_detail', id=event.event_id)
#     else:
#         form = EventForm(instance=event)
    
#     context = {
#         'form': form,
#         'event': event
#     }
#     return render(request, 'TicketStore/update_event.html', context)