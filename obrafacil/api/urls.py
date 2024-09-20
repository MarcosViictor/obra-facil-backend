
from django.urls import path
from .views import (
    ObraListCreateView, ObraDetailView,
    EmpresaListCreateView, EmpresaDetailView,
    AcompanhamentoListCreateView, AcompanhamentoDetailView,
    MaterialListCreateView, MaterialDetailView
)

urlpatterns = [
    # Obra URLs
    path('obras/', ObraListCreateView.as_view(), name='obra-list-create'),
    path('obras/<int:pk>/', ObraDetailView.as_view(), name='obra-detail'),

    # Empresa URLs
    path('empresas/', EmpresaListCreateView.as_view(), name='empresa-list-create'),
    path('empresas/<int:pk>/', EmpresaDetailView.as_view(), name='empresa-detail'),

    # Acompanhamento URLs
    path('acompanhamentos/', AcompanhamentoListCreateView.as_view(), name='acompanhamento-list-create'),
    path('acompanhamentos/<int:pk>/', AcompanhamentoDetailView.as_view(), name='acompanhamento-detail'),

    # Material URLs
    path('materiais/', MaterialListCreateView.as_view(), name='material-list-create'),
    path('materiais/<int:pk>/', MaterialDetailView.as_view(), name='material-detail'),
]