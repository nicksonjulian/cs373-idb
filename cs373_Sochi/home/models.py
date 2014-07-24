from django.db import models

class Athlete(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = (
        ('', 'None'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country =  models.ForeignKey('Country')
    #Need to check that this is correct
    gender = models.CharField(max_length=10,
                              choices=GENDER_CHOICES,
                              default='')
    height = models.CharField(max_length=30, blank=True, null=True)
    weight = models.CharField(max_length=30, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    picture = models.CharField(max_length=50, blank=True, null=True)
    video = models.CharField(max_length=50, blank=True, null=True)
    gold_medals = models.ManyToManyField('Events', blank=True, related_name='athlete_gold')
    silver_medals = models.ManyToManyField('Events', blank=True, related_name='athlete_silver')
    bronze_medals = models.ManyToManyField('Events', blank=True, related_name='athlete_bronze')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.first_name + " "  + self.last_name

class Events(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    icon = models.CharField(max_length=20, blank=True, null=True)
    gold_medalists =  models.ManyToManyField(Athlete, blank=True, related_name='events_gold')
    silver_medalists =  models.ManyToManyField(Athlete, blank=True, related_name='events_silver')
    bronze_medalists =  models.ManyToManyField(Athlete, blank=True, related_name='events_bronze')

    class Meta:
        ordering = ['sport','name']

    def __str__(self):
        return self.sport + ": " + self.name

class Country(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    total_gold_medals = models.IntegerField(blank=True, null=True)
    total_silver_medals = models.IntegerField(blank=True, null=True)
    total_bronze_medals = models.IntegerField(blank=True, null=True)
    athletes = models.ManyToManyField(Athlete, blank=True, null=True, related_name='country_athletes')
    country_code = models.CharField(max_length=10, blank=True, null=True)
    coordx = models.FloatField(blank=True, null=True)
    coordy = models.FloatField(blank=True, null=True)
    coordz = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    #For Events with medals, load dynamically (?)
    def __str__(self):
        return self.name
