from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('upload/', views.upload, name='upload')
]
