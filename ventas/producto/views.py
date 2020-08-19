from django.shortcuts import render ,redirect,get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import Producto
from  django.db.models import Q


class home(ListView):
    model = Producto
    template_name='producto/home.html'
    context_object_name='productos'
    ordering=['-fecha']
    paginate_by=8

class ProductoListView(ListView):
    model = Producto
    template_name='producto/productos.html'
    context_object_name='productos'
    ordering=['-fecha']
    paginate_by = 8


class SearchResultsView(ListView):
    model= Producto
    template_name='producto/search_result.html'
    context_object_name='productos'
    def get_queryset(self):
        filter_val=self.request.GET.get('filter',)
        new_context=Producto.objects.filter(
                Q(marca__icontains=filter_val)|
                Q(modelo__icontains=filter_val)|
                Q(precio__icontains=filter_val)
             )
        return new_context
    paginate_by = 8

class ProductoDetalle(DetailView):
    model=Producto
    template_name='producto/producto_detalle.html'




class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    fields = ['titulo', 'descripcion','marca','modelo','precio','fecha','foto1','foto2','foto3','foto4','foto5']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class ProductoDetailView(DetailView):
    model = Producto


class UserProductoListView(ListView):
    model=Producto
    template_name='producto/user_productos.html'
    context_object_name='productos'
    paginate_by=3

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Producto.objects.filter(autor=user).order_by('-fecha')

class ProductoUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Producto
    fields=['titulo', 'descripcion','marca','modelo','precio','fecha','foto1','foto2','foto3','foto4','foto5']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        producto=self.get_object()
        if self.request.user==producto.autor:
            return True
        return False

class ProductoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    success_url = '/'

    def test_func(self):
        producto = self.get_object()
        if self.request.user == producto.autor:
            return True
        return False