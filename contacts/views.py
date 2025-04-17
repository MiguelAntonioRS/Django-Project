from django.shortcuts import render
from django.views import generic
from contacts.models import Contact

class ContactListView(generic.ListView):
    model = Contact