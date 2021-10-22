from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from blog.models import *

# Create your views here.

class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class BlogList(ListView):
    model = publicaciones

class BlogDetail(DetailView):
    model = publicaciones













