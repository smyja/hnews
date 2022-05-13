from django.contrib import admin
from .models import Stories, Comment
# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    readonly_fields = ('synced',)
admin.site.register(Stories, StoryAdmin)
admin.site.register(Comment)
