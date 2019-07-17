from django.contrib import admin
from . import models;

# Register your models here.

admin.site.register(models.Contact)
admin.site.register(models.ContactType)
admin.site.register(models.ContactMoment)
admin.site.register(models.ConnectionType)
admin.site.register(models.Person)
admin.site.register(models.Connection)

