from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from formLesson1.form import ContactForm

class HomeTemplateView(TemplateView):
    template_name = "formLesson1/home.html"
# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(f"Nome: {form.cleaned_data['name']}")
            print(f"Cognome: {form.cleaned_data['last_name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Contenuto: {form.cleaned_data['content']}")
            return HttpResponse('Grazie per averci contattato')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'formLesson1/contact_page.html', context)