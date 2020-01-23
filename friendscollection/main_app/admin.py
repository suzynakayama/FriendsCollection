from django.contrib import admin
from .models import Friend, Feeding, Interest, Photo

# Register your models here.
admin.site.register(Friend)
admin.site.register(Feeding)
admin.site.register(Interest)
admin.site.register(Photo)