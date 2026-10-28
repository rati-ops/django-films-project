from django.urls import path
from . import views

app_name = "exam_app"

urlpatterns = [
    path('', views.home, name='home'),
    

]