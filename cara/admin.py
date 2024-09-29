from django.contrib import admin
from .models import BranchData, Node, Vetv


@admin.register(BranchData)
class BranchDataAdmin(admin.ModelAdmin):
    list_display = ['ip', 'iq', 'np', 'name', 'id_sk11', 'svg_id']
    search_fields = ['name']


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    search_fields = ['number', 'status']


@admin.register(Vetv)
class VetvAdmin(admin.ModelAdmin):
    search_fields = ['name', 'status']
