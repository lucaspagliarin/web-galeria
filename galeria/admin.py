from django.contrib import admin
from .models import Collection, Photo, Tag
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
  list_display = ("archive", "collection", "author", "isFavorite")

class CollectionAdmin(admin.ModelAdmin):
  list_display = ("title", "author")


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag)