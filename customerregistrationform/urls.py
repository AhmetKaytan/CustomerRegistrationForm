from django.conf.urls import include, url
from django.contrib import admin
from customerregistration import views 
from django.urls import path
from customerregistration.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.main_view.as_view(template_name="main.html"), name='main'),
    path('create/', views.customer_create_view.as_view(template_name="create.html"), name='create'),
    path('update/<int:id>', views.customer_update_view.as_view(template_name="update.html"), name='update'),
    path('detail/<int:id>', views.customer_detail_view.as_view(template_name="detail.html"), name='detail'),
    path('delete/<int:id>', views.customer_delete_view.as_view(template_name="delete.html"),name='delete')
]