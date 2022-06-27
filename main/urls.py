from django.urls import path 
from .views import Main_Page,Season_Page,SeriesViewClass

urlpatterns = [ 
	path('',Main_Page.as_view(),name='sitepage'),
    path('<slug:slug>',Season_Page.as_view(),name='Season_url'),
    path('<slug:slug>/<int:season_num>',SeriesViewClass.as_view(),name='Series_url'),
]