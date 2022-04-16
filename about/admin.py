from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Profile, Interest


class ProfileAdmin(SingleModelAdmin):
    list_display = ['name']


class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Profile, ProfileAdmin),
admin.site.register(Interest, InterestAdmin)
