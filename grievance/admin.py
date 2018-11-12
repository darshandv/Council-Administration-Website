from django.contrib import admin
from .models import Post,Comment,Event,TimePoint

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(TimePoint)