from django.urls import path
from app1.views import *
urlpatterns=[
    path('second/',second,name='second')
]
app_name='something1'