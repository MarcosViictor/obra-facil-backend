
from django.urls import path
from .views import (
    GerenteDeObraListCreateView, GerenteDeObraDetailView,
    MestreDeObraListCreateView, MestreDeObraDetailView,
    ObraListCreateView, ObraDetailView,
    EmpresaListCreateView, EmpresaDetailView,
    AcompanhamentoListCreateView, AcompanhamentoDetailView,
    MaterialListCreateView, MaterialDetailView
)

urlpatterns = [
    # GerenteDeObra URLs
    path('gerentes/', GerenteDeObraListCreateView.as_view(), name='gerente-list-create'),
    path('gerentes/<int:pk>/', GerenteDeObraDetailView.as_view(), name='gerente-detail'),

    # MestreDeObra URLs
    path('mestres/', MestreDeObraListCreateView.as_view(), name='mestre-list-create'),
    path('mestres/<int:pk>/', MestreDeObraDetailView.as_view(), name='mestre-detail'),

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