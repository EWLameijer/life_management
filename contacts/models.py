from django.db import models

# Create your models here.

NAME_LENGTH = 30
DESCRIPTION_LENGTH = 20

class Person(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name


class ContactType(models.Model):
    description = models.CharField(max_length=DESCRIPTION_LENGTH, unique=True)

    def __str__(self):
        return self.description


class ContactMoment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f'{self.contact.person.name}:' + event_and_date(self)

    def event_and_date(self):
        return f'{self.type} {self.date}'

    class Meta:
        unique_together = ('contact', 'date')


class ConnectionType(models.Model):
    description = models.CharField(max_length=DESCRIPTION_LENGTH, unique=True)

    def __str__(self):
        return self.description

  
class Connection(models.Model):
    subject = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='subject')
    relationship = models.ForeignKey(ConnectionType, on_delete=models.CASCADE)
    other_person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='other')

    def __str__(self):
        return "{} - {} of {}".format(
            self.subject.name,
            self.relationship.description,
            self.other_person.name)

    class Meta:
        unique_together = ('subject', 'other_person')
    







    
    
