from django import  http
from django.core import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.query_utils import Q
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.views.generic import  View,ListView
from django.db.models import Q
from .models import Customer
from .forms import CustomerForm, paginationForm
from typing import Any



class login_view(View):
    template_name = 'login.html'


class main_view(ListView):
    template_name = 'main.html'

    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.all()
        paginate_by=5
        # Searching
        query=request.GET.get('q')
        if query:
            Customers=Customers.filter(
            Q(name__icontains=query) | 
            Q(id__icontains=query) | 
            Q(surname__icontains=query) | 
            Q(tc_no__icontains=query)|
            Q(phone_no__icontains=query)|
            Q(city__icontains=query)|
            Q(district__icontains=query)
        ).distinct()

        return render(request, 'main.html', {'Customers': Customers})
    """ def post(self, request, *args, **kwargs):
        customer_list = Customer.objects.all()
        paginate = request.POST.get('p')
        paginator=Paginator(customer_list,paginate)
        try:
            customers = paginator.page(paginate)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            customers = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            customers = paginator.page(paginator.num_pages)
        return render(request, 'main.html', ) """
     

class customer_detail_view(View):
    template_name = 'detail.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id = kwargs['id'])
        context={
            'Customer': Customers,
        }
        return render(request, 'detail.html', context)


class customer_create_view(View):
    template_name = 'create.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        form = CustomerForm()
        context={
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


class customer_update_view(View):
    template_name = 'update.html'   
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id=kwargs['id'])
        form = CustomerForm(request.POST or None, instance=Customers)
        context = {
            'form': form
        }
        return render(request, 'form.html', context)

    def post (self, request, *args, **kwargs):
        Customers = Customer.objects.get(id=kwargs['id'])
        form = CustomerForm(request.POST or None, instance=Customers)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully")
            return HttpResponseRedirect('/')
        context = {
            'form': form
        }
        return render(request, 'form.html', context)


class customer_delete_view(View):
    template_name = 'delete.html'
    def get(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        Customers = Customer.objects.get(id = kwargs['id'])
        Customer.delete(Customers)
        messages.success(request, "Customer deleted successfully")
        return redirect('/')

