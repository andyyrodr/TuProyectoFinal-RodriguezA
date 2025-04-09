from django.urls import path

from . import views

app_name = "historia"

urlpatterns = [
    path("", views.index, name="index"),
    path("categoria/list/", views.categoria_list, name="categoria_list"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),

]

urlpatterns += [
    path("historia/list/", views.HistoriaListView.as_view(), name="historia_list"),
    path("historia/create/", views.HistoriaCreateView.as_view(), name="historia_create"),
    path("historia/update/<int:pk>", views.HistoriaUpdateView.as_view(), name="historia_update"),
    path("historia/detail/<int:pk>", views.HistoriaDetailView.as_view(), name="historiadetail"),
    path("historia/delete/<int:pk>", views.HistoriaDeleteView.as_view(), name="historia_delete"),
    ]