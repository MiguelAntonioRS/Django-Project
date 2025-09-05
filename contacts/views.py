from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from contacts.models import Contact
from django.db.models import QuerySet

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5
    
    def get_queryset(self) -> QuerySet[any]:
        if self.request.GET.get('s'):
            return Contact.objects.filter()
        
        return super().get_queryset()
    
class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth_date', 'phone')
    success_url = reverse_lazy('contact_list')
    
class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth_date', 'phone')
    success_url = reverse_lazy('contact_list') 
    
class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list') 