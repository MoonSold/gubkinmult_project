from django.views.generic import ListView,CreateView,DetailView,View
from django.views.generic.edit import FormMixin
from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login 
from django.http import JsonResponse
# Create your views here.
 
now = None

class Main_Page(ListView): 
    model = All_Mult
    template_name = 'main/mainpage.html'
    context_object_name = 'mults'

class Season_Page(View):
    def get(self,request,slug):
        template = 'main/season.html' 
        season_inf = All_Season.objects.filter(mult = All_Mult.objects.get(URL=slug))
        now = slug
        context = {'season':season_inf,'slug':slug}
        return render(request, template, context)



class SeriesViewClass(FormMixin,DetailView): 
    model = All_Season
    template_name = 'main/series.html'

    def get_success_url(self,**kwargs): 
        return reverse_lazy('Series_url',kwargs = {'slug':self.get_object().mult.URL,'season_num':self.get_object().season_num})
 
    # def get_queryset(self,*kwargs):
    #     return All_Series.objects.filter(season = )

    def get_context_data(self,**kwargs): 
        context = super(SeriesViewClass, self).get_context_data(**kwargs)
        context['season'] = All_Season.objects.filter(pk = self.get_object().id)    
        context['series'] = All_Series.objects.filter(season = self.get_object())
        context['first'] = All_Series.objects.filter(season = self.get_object()).filter(series_num = 1)
        return context


