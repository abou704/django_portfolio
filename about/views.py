from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import Profile
from experience.models import Employment, Education
from skillset.models import Skill, Software
from work.models import Client, Project
from django.db.models import Q, Count


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all().first()
        context['employments'] = Employment.objects.all()
        context['educations'] = Education.objects.all()
        context['skills'] = Skill.objects.all()
        context['software'] = Software.objects.all()
        context['clients'] = Client.objects.all()
        context['projects'] = Project.objects.all()
        return context
