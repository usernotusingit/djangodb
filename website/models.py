from django.db import models

# Create your models here.

class Member(models.Model):
    fname = models.CharField(max_length= 200)
    lname = models.CharField(max_length= 200)
    email = models.EmailField(max_length= 200)
    passwd = models.CharField(max_length= 200)
    


    def __str__(self):
        return self.fname +' '+ self.lname
    
class Venue(models.Model):
    name = models.CharField('venue name',max_length = 200)
    adress = models.CharField(max_length = 200)
    zip_code= models.CharField('zip code', max_length = 200)
    phone_number= models.CharField('contact phone', max_length = 25)
    webaddress= models.URLField('website address')
    email_address = models.EmailField('email')


    def __str__(self):
        return self.name
    
class MyClubUser(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField('user email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name      


class Event(models.Model):
    name = models.CharField('event name',max_length = 200)
    event_date= models.DateTimeField('event date')
    venue= models.ForeignKey(Venue, blank = True, null = True, on_delete=models.CASCADE)
    manager= models.CharField(max_length = 200)
    descrpition= models.TextField(blank = True)
    attendees = models.ManyToManyField(MyClubUser, blank = True)


    def __str__(self):
        return self.name

