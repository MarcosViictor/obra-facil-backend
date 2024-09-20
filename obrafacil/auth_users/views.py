from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import GerenteDeObra, MestreDeObra
from .serializers import GerenteDeObraRegisterSerializer, LoginSerializer, MestreDeObraRegisterSerializer

# View para registro de Gerente de Obra
class GerenteDeObraRegisterView(generics.CreateAPIView):
    serializer_class = GerenteDeObraRegisterSerializer
    

# View para registro de Mestre de Obra
class MestreDeObraRegisterView(generics.CreateAPIView):
    serializer_class = MestreDeObraRegisterSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Gera os tokens JWT
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
