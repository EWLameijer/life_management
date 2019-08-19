from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


from .models import Contact, ContactMoment, Person

# Create your views here.

NO_CONTACTS_RECORDED = 'no contacts recorded'

def persons_to_json(request):
    data = serializers.serialize("json", Person.objects.all())
    return HttpResponse(data)

def persons(request):
    person_set = Person.objects.all()
    person_list = [(p.name + '<br>') for p in person_set]
    return HttpResponse(person_list)

def contacts(request):
    contact_list = list(Contact.objects.all())
    contact_data = {c.person.name: last_contact_moment(c) for c in contact_list}
    # now I have a dict of name: str to contactMoment: ContactMoment
    never_contacted = { name: moment for (name, moment) in contact_data.items()
                        if moment == NO_CONTACTS_RECORDED }
    contacted_unsorted = [ (name, moment) for (name, moment) in contact_data.items()
                  if moment != NO_CONTACTS_RECORDED ]
    # contact_tuples = sorted(contact_data.items(), key=lambda x: x[1].date)
    never_contacted_string = '<br>'.join([f'{name}: {NO_CONTACTS_RECORDED}' for
                                   name in never_contacted.keys()])
    contacted = sorted(contacted_unsorted, key=getMoment, reverse=True)
    contacted_string = '<br>'.join([f'{name}: {moment}' for (name, moment) in contacted])
    return HttpResponse(never_contacted_string + '<br><br>' + contacted_string)

def getMoment(contactTuple):
    return contactTuple[1]


def last_contact_moment(contact):
    moment_set = ContactMoment.objects.filter(contact=contact)
    if not moment_set: return NO_CONTACTS_RECORDED
    return moment_set.order_by('date')[0]
    
