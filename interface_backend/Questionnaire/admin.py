# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Reponse

@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "age", "date_creation")
    search_fields = ("nom", "email")
