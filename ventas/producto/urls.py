from django.urls import path
from .views import ( 
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    UserProductoListView,
    ProductoUpdateView,
    ProductoDeleteView,
    home,
    ProductoDetalle,
    SearchResultsView
    
)
from . import views

urlpatterns = [
    path('', ProductoListView.as_view(), name='listar-producto'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('productos/', home.as_view(), name='home'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('productodetalle/<int:pk>/', ProductoDetalle.as_view(), name='producto-detalle'),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('user/<str:username>', UserProductoListView.as_view(), name='user-productos'),
    path('producto/<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),
]
