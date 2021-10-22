from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


#def contact(request):
    #return render(request, 'contact/contact.html', {})

class Contact(TemplateView):
    template_name = "contact/contact.html"