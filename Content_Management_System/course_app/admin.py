from django.contrib import admin
from .models import Course, Topic, CustomUser

# Register your models here.
admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(CustomUser)
