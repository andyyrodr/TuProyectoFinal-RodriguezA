from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from . import forms, models


def index(request):
    return render(request, "historia/index.html")



def categoria_list(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        queryset = models.Categoria.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = models.Categoria.objects.all()
    context = {"object_list": queryset}
    return render(request, "historia/categoria_list.html", context)


def categoria_create(request):
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("historia:historia_create")
    return render(request, "historia/categoria_form.html", {"form": form})

class HistoriaListView(ListView):
    model = models.historia
    template_name = "historia/historia_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = models.historia.objects.filter(nombre__icontains=busqueda)
        else:
            queryset = models.historia.objects.all()
        return queryset


class HistoriaCreateView(CreateView):
    model = models.historia
    form_class = forms.HistoriaForm
    success_url = reverse_lazy("historia:historia_list")
    


class HistoriaUpdateView(UpdateView):
    model = models.historia
    template_name = "historia/historia_update.html"  # <-- nuevo nombre
    fields = ['nombre', 'autor', 'fecha', 'categoria', 'contenido']
    success_url = reverse_lazy("historia_list")
    


class HistoriaDetailView(DetailView):
    model = models.historia
    template_name = "historia/historia_detail.html"
    success_url = reverse_lazy("historia_list")


class HistoriaDeleteView(DeleteView):
    model = models.historia
    template_name = "historia/historia_confirm_delete.html"
    success_url = reverse_lazy("historia:historia_list")


