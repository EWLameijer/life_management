from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import Contact, ContactMoment, Person

# Create your views here.

def persons_to_json(request):
    data = serializers.serialize("json", Person.objects.all())
    return HttpResponse(data)

def persons(request):
    person_set = Person.objects.all()
    person_list = [(p.name + '<br>') for p in person_set]
    return HttpResponse(person_list)

def contacts(request):
    contact_list = list(Contact.objects.all())
    contact_names = [f'{c.person.name}: {last_contact_moment(c)} <br>'
                     for c in contact_list]
    return HttpResponse(contact_names)
    
def last_contact_moment(contact):
    moment_set = ContactMoment.objects.filter(contact=contact)
    if not moment_set: return 'no contacts recorded'
    return moment_set.order_by('date')[0].event_and_date()
    
