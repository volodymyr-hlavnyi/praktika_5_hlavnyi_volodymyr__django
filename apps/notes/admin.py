from django.contrib import admin
from apps.notes import models


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SecretKey)
class SecretKeyAdmin(admin.ModelAdmin):
    pass
