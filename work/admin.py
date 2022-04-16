from django.contrib import admin
from .models import Client, Project


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'type', 'date', 'completed', 'status')
    list_filter = ('skills', 'type', 'client_name')
    search_fields = ['client_name', 'date']


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
