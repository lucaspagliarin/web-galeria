from django.contrib import admin
from .models import Collection, Photo, Tag
# Register your models here.

admin.site.register(Collection)
admin.site.register(Photo)
admin.site.register(Tag)