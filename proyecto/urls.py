"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from historia import views










urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    
   
    
    
]

urlpatterns += [

    path("categoria/list/", views.categoria_list, name="categoria_list"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    path("categoria/update/<int:pk>", views.categoria_update, name="categoria_update"),
   path("categoria/delete/<int:pk>/", views.categoria_delete, name="categoria_delete"),

]

urlpatterns += [
    path("historia/list/", views.HistoriaListView.as_view(), name="historia_list"),
    path("historia/create/", views.HistoriaCreateView.as_view(), name="historia_create"),
    path("historia/update/<int:pk>", views.HistoriaUpdateView.as_view(), name="historia_update"),
    path("historia/detail/<int:pk>", views.HistoriaDetailView.as_view(), name="historia_detail"),
    path("historia/delete/<int:pk>/", views.HistoriaDeleteView.as_view(), name="historia_confirm_delete"),
    path('historia/', include(('historia.urls', 'historia'), namespace='historia')),



    ]
