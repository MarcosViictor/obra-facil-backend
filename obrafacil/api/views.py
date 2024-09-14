from django.shortcuts import render
from rest_framework import generics
from .models import GerenteDeObra, MestreDeObra, Obra, Empresa, Acompanhamento, Material
from .serializers import GerenteDeObraSerializer, MestreDeObraSerializer, ObraSerializer, EmpresaSerializer, AcompanhamentoSerializer, MaterialSerializer

class GerenteDeObraListCreateView(generics.ListCreateAPIView):
    queryset = GerenteDeObra.objects.all()
    serializer_class = GerenteDeObraSerializer

class GerenteDeObraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GerenteDeObra.objects.all()
    serializer_class = GerenteDeObraSerializer

class MestreDeObraListCreateView(generics.ListCreateAPIView):
    queryset = MestreDeObra.objects.all()
    serializer_class = MestreDeObraSerializer

class MestreDeObraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MestreDeObra.objects.all()
    serializer_class = MestreDeObraSerializer

class ObraListCreateView(generics.ListCreateAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class ObraDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class AcompanhamentoListCreateView(generics.ListCreateAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer