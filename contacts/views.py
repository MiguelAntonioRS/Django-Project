from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from contacts.models import Contact

class ContactListView(generic.ListView):
    model = Contact
    
class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('name', 'email', 'birth_date', 'phone')
    success_url = reverse_lazy('contact_list')
    
class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('name', 'email', 'birth_date', 'phone')
    success_url = reverse_lazy('contact_list')