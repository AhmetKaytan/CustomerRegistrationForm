from django import  http
from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.views.generic import  View,ListView
from django.db.models import Q
from typing import Any

from .models import Customer
from .forms import CustomerForm

default_paginate = 6

class loginView(View):
    template_name = 'login.html'


class mainView(ListView):
    template_name = 'main.html'
   
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.all()
        customer_list = Customer.objects.all()
        paginator = Paginator(customer_list, default_paginate)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Searching
        query = request.GET.get('q')
        if query:
            Customers = Customers.filter(
            Q(name__icontains=query) | 
            Q(id__icontains=query) | 
            Q(surname__icontains=query) | 
            Q(tc_no__icontains=query)|
            Q(phone_no__icontains=query)|
            Q(city__icontains=query)|
            Q(district__icontains=query)
            ).distinct()

        context = {
                'Customers' : page_obj
            }
        return render(request, 'main.html', context)        

     
class customerDetailView(View):
    template_name = 'detail.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id = kwargs['id'])
        context = {
            'Customer': Customers,
        }
        return render(request, 'detail.html', context)


class customerCreateView(View):
    template_name = 'create.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        form = CustomerForm()
        context = {
            'form': form,
        }
        return render(request, 'form.html', context)

    def post(self, request, *args, **kwargs):
        form = CustomerForm(request.POST or None)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            messages.success(request, "Customer created successfully")
            return HttpResponseRedirect('/')
        
        return render(request, 'form.html', context)


class customerUpdateView(View):
    template_name = 'update.html'   
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id=kwargs['id'])
        form = CustomerForm(request.POST or None, instance=Customers)
        context = {
            'form': form
        }
        return render(request, 'form.html', context)

    def post (self, request, *args, **kwargs):
        Customers = Customer.objects.get(id = kwargs['id'])
        form = CustomerForm(request.POST or None, instance = Customers)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully")
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'form.html', context)


class customerDeleteView(View):
    template_name = 'delete.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id = kwargs['id'])
        Customer.delete(Customers)
        messages.success(request, "Customer deleted successfully")
        return redirect('/')

