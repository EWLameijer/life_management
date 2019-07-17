from django.db import models

# Create your models here.

NAME_LENGTH = 30
DESCRIPTION_LENGTH = 20

class Person(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.name


class ContactType(models.Model):
    description = models.CharField(max_length=DESCRIPTION_LENGTH)

    def __str__(self):
        return self.description


class ContactMoment(models.Model):
    name = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} (on {})".format(self.name, self.type, self.date)


class ConnectionType(models.Model):
    description = models.CharField(max_length=DESCRIPTION_LENGTH)

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
    







    
    
