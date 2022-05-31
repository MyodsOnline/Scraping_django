from django.contrib import admin

from .models import Message, MessageAuthor, MessageTag


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('boss_name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class MessageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Message, MessageAdmin)
admin.site.register(MessageAuthor, AuthorAdmin)
admin.site.register(MessageTag, MessageAdmin)
