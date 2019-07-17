"""crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'predictions'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('top/', views.top_predictions, name='top_predictions'),
    path('predictions/<slug:slug>/', views.prediction_view, name='prediction'),
    path('add_prediction/', views.add_prediction, name='add_prediction'),
]
