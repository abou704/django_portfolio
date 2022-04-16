from django.contrib import admin
from .models import Skill, Software


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    search_fields = ['name']


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    search_fields = ['name']


admin.site.register(Skill, SkillAdmin)
admin.site.register(Software, SoftwareAdmin)
