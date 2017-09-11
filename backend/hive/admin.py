from django.contrib import admin
from django.conf import settings
# Register your models here.
from .models import Treatment, BG, Dose, Extended_Bolus, Meal

class BgInline(admin.TabularInline):
    model = BG
    extra = 1

class DoseInline(admin.TabularInline):
    model = Dose
    extra = 1

class MealInline(admin.TabularInline):
    model = Meal
    extra = 1

class TreatmentAdmin(admin.ModelAdmin):
    fields = ['owner','source']
    inlines = [BgInline, DoseInline, MealInline]

admin.site.register(Treatment,TreatmentAdmin)
