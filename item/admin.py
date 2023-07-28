from django.contrib import admin
from .models import *

# Register your models here.
class Cat(admin.ModelAdmin):
    list_display=('name', 'description')

admin.site.register(Catagory, Cat)

# admin.site.register(Catagory)
admin.site.register(Product)