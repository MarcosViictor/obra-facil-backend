from django.urls import path
from .views import GerenteDeObraRegisterView, MestreDeObraRegisterView, LoginView

urlpatterns = [
    path('register/gerente/', GerenteDeObraRegisterView.as_view(), name='register-gerente'),
    path('register/mestre/', MestreDeObraRegisterView.as_view(), name='register-mestre'),
    path('login/', LoginView.as_view(), name='login'),  # Certifique-se de que esta linha está correta
]
