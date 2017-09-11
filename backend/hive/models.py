from django.db import models
from django.contrib.auth.models import User #this line is from http://www.b-list.org/weblog/2006/jun/06/django-tips-extending-user-model/
from decimal import Decimal
# Create your models here.

"""

Models:

Treatment:
    User
    Timestamp
    BG: BG
    Based on: CGM graph, CGM reading, BG metter reading
    Meal:
    Insulin: [Insulin Doses]
    Notes

BG:
    Level
    User
    Timestamp

Dose:
    User
    Amount
    Extended
    Prebolus?

Meal:
    Snack?
    Carbs
    Photo
    Note


"""



class Treatment(models.Model):
    METER = "M"
    CGM_GRAPH = "G"
    CGM_READING = "C"
    SOURCE_CHOICES = (
        (METER, "Meter reading"),
        (CGM_READING, "CGM reading"),
        (CGM_GRAPH, "CGM graph"),
        (None, "No source set")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('date submitted')
    source = models.CharField(max_length=1,choices=SOURCE_CHOICES,default=METER)

class BG(models.Model):
    assoc_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE,verbose_name="Associated treatment")
    level = models.PositiveIntegerField(verbose_name="BG")

class Dose(models.Model):
    assoc_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, verbose_name="Associated treatment")
    amount = models.DecimalField(max_digits=4,decimal_places=4)
    is_prebolus = models.BooleanField(verbose_name='Prebolus')
    carb_ratio = models.DecimalField(max_digits=2,decimal_places=2,verbose_name="Carb ratio (1:__)")
    isf = models.PositiveIntegerField(verbose_name="ISF",default=75)


class Extended_Bolus(models.Model):
    duration = models.PositiveIntegerField()
    percent_now = models.DecimalField(max_digits=2,decimal_places=2)
    percent_later = models.DecimalField(max_digits=2,decimal_places=2)
    assoc_dose = models.ForeignKey(Dose,on_delete=models.CASCADE)

class Meal(models.Model):
    BREAKFAST = 'B'
    LUNCH = 'L'
    DINNER = 'D'
    BEDTIME = 'N'
    SNACK = 'S'
    MEAL_CHOICES = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner"),
        (BEDTIME, "Bedtime"),
        (SNACK, "Snack"),
        (None, "No meal set")
    )
    assoc_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    time_of_day = models.CharField(max_length=1,choices=MEAL_CHOICES)
    carbs = models.PositiveIntegerField()
    picture = models.ImageField(blank=True)
    note = models.TextField(blank=True)
