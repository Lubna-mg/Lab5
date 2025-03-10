from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="bookmodules.index"),
    path('html5/links/', views.html5_links, name="bookmodules.html5_links"),
    path('html5/text/formatting/', views.text_formatting, name="bookmodules.text_formatting"),
    path('html5/listing/', views.listing, name="bookmodules.listing"),
    path('html5/tables/', views.tables, name="bookmodules.tables"),
]
