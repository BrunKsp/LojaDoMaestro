from django.urls import path

from . import views
from accounts.views import Cliente

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='register'),
    path('cliente/',Cliente.clienteView, name='cliente'),
    path('dados/',Cliente.dadosView, name='dados'),
]