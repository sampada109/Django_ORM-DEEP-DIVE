from django.contrib import admin
from core.models import Restaurant, Sales, Rating

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Sales)