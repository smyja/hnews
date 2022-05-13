from django.contrib import admin
from .models import Stories, Comment
# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'url', 'time')
    readonly_fields = ('synced',)
admin.site.register(Stories, StoryAdmin)
admin.site.register(Comment)
