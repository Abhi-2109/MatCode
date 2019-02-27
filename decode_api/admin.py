from django.contrib import admin

from . import models

# Register your models here.


admin.site.register(models.UserProfile)
admin.site.register(models.Problem)
admin.site.register(models.Solution)
admin.site.register(models.Stats)