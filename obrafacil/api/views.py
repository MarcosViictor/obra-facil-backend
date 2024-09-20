from django.shortcuts import render
from rest_framework import generics
from .models import  Obra, Empresa, Acompanhamento, Material
from .serializers import  ObraSerializer, EmpresaSerializer, AcompanhamentoSerializer, MaterialSerializer

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