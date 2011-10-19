from django.db import models
from django.forms import ModelForm

#TODO -Add one-to-many field between User and Trip Objects

class Trip(models.Model):
    destination = models.CharField(max_length=150)
    start_time = models.DateField(verbose_name="Start time(mm/dd/yyyy)")
    end_time = models.DateField(verbose_name="End time(mm/dd/yyyy)")
    #Water type can be river, lake, creek++
    water_type = models.CharField(max_length=150)
    comment = models.CharField(max_length=200)
    
    def __unicode__(self):
        #Displays destination
        #number of days the trip lasted and when it started.
        #Used as an identifier when you create a new fish
        time_delta = self.start_time - self.end_time
        num_days = time_delta.days
        return '%s -- %s days -- started: %s' %(self.destination,
                                                num_days,
                                                self.start_time
                                               )

class Fish(models.Model):
    trip = models.ForeignKey(Trip)
    fish_type = models.CharField(max_length=100)
    weight = models.IntegerField(verbose_name="Weight in gram")
    length = models.IntegerField(verbose_name="length in cm")
    #Fly, spinner...
    lure = models.CharField(max_length=100)
    comment = models.TextField(max_length=200)


class TripForm(ModelForm):
    #Class created a django form out of a Trip object
    class Meta:
        model = Trip

class FishForm(ModelForm):
    #Class created a django form out of a Fish object
    class Meta:
        model = Fish
