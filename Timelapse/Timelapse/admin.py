from django.contrib import admin
from .models import TimelapseImage

class TimelapseAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(TimelapseImage, TimelapseAdmin)