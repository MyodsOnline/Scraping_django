from django.contrib import admin
from .models import BranchData


@admin.register(BranchData)
class BranchDataAdmin(admin.ModelAdmin):
    list_display = ['ip', 'iq', 'np', 'name', 'id_sk11', 'svg_id']
    search_fields = ['name']
