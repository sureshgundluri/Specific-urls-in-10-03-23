from django.urls import path
from app.views import *
urlpatterns=[
    path('first/',first,name='first')
]
app_name='something'