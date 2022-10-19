from django.contrib import admin
from .models import Empreco
# Register your models here.
@admin.register(Empreco)
class Emprecoadmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email']