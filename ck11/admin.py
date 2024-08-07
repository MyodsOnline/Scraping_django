from django.contrib import admin

from .models import UIDMapping, DatetimeValues


admin.site.register(UIDMapping)
admin.site.register(DatetimeValues)
