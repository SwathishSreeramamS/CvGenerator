from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexPage,name='index'),
    path('accept/',views.acceptPage,name='accept'),
    path('resume/',views.resumePage,name='resume'),
]
