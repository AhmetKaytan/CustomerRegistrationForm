from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from customerregistration import views 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.mainView.as_view(template_name = "main.html"), name = 'main'),
    path('create/', views.customerCreateView.as_view(template_name = "create.html"), name = 'create'),
    path('update/<int:id>', views.customerUpdateView.as_view(template_name = "update.html"), name = 'update'),
    path('detail/<int:id>', views.customerDetailView.as_view(template_name = "detail.html"), name = 'detail'),
    path('delete/<int:id>', views.customerDeleteView.as_view(template_name = "delete.html"), name = 'delete')
]