from django.urls import path

from .views import home,about

urlpatterns =[
    path('',home.as_view(),name='home'),
    path('about/<id>',about.as_view(),name='about')
]