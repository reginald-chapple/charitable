from django.urls import path

from . import views

urlpatterns = [
    path('not-found/', views.not_found, name='not-found'),
    path('forbidden/', views.forbidden, name='forbidden'),
    path('general-error/', views.server_error, name='server-error'),
]
