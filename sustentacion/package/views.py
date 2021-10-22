from django.shortcuts import render, redirect
from package.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from package.forms import PackageForms
# Create your views here.

class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)




class PackageListView(StaffRequiredMixin, ListView):
    model = paquete



class PackageDetailView(StaffRequiredMixin, DetailView):
    model = paquete

class PackageCreate(StaffRequiredMixin, CreateView):
    model = paquete
    fields = ['nombre', 'precio', 'comentario', 'Contenido', 'usuario', 'categoria', 'imagen']
    success_url = reverse_lazy('package')


class PackageUpdate(StaffRequiredMixin, UpdateView):
    model = paquete
    fields = ['nombre', 'precio', 'comentario', 'Contenido', 'imagen', 'usuario', 'categoria']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id])+'?ok'

class PackageDelete(StaffRequiredMixin, DeleteView):
    model = paquete
    success_url = reverse_lazy('package')

