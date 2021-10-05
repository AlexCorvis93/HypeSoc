from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Profile, Post


class ProfilePage(TemplateView):
    template_name = 'profile.html'

    def get_p(self, request):
        person = Profile.objects.all()
        ctx = {
            'profile': person
        }

        return JsonResponse(ctx)
        return render(request, self.template_name, ctx)






