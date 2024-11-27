from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.AboutMeViewSet.as_view({'get': 'list',}), name='about-me'),
    path('contacts/', views.ContactsViewSet.as_view({'get': 'list', }), name='contacts'),
]