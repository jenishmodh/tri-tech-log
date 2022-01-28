from django.urls import path
from .views import *
urlpatterns = [
    path('',Login,name="login"),
    path('sinup/',Sinup,name="sinup"),
    path('index/',Home,name="index"),
    path('Forget_ps/',Forget_ps,name="Forget_ps"),
    path('C_otp/',C_otp,name="C_otp"),
    path('New_pass/',New_pass,name="New_pass"),
]
