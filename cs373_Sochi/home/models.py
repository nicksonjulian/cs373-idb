from django.db import models

class Athlete(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        ('', 'None'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country =  models.ForeignKey('Country')
    #Need to check that this is correct
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='')
    birthdate = models.DateField(blank=True, null=True)
    gold_medals = models.ManyToManyField(Events, blank=True)
    silver_medals = models.ManyToManyField(Events, blank=True)
    bronze_medals = models.ManyToManyField(Events, blank=True)

class Events(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    gold_medalists =  models.ManyToManyField(Athlete, blank=True)
    silver_medalists =  models.ManyToManyField(Athlete, blank=True)
    bronze_medalists =  models.ManyToManyField(Athlete, blank=True)

class Country(models.Model):
    name = models.CharField(max_length=150)
    #TODO: Dynamically find total medals
    total_gold_medals = models.IntegerField(blank=True)
    total_silver_medals = models.IntegerField(blank=True)
    total_bronze_medals = models.IntegerField(blank=True)
    athletes = models.ManyToManyField(Athlete, blank=True)
    description = models.CharField(max_length=500)
    #For Events with medals, load dynamically (?)
