from django.shortcuts import render
from django.views import generic
from contacts.models import Contact

class ContactListView(generic.ListView):
    model = Contact
    
class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('name', 'email', 'birth_date', 'phone')