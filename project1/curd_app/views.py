from django.shortcuts import render, redirect
from .forms import IndiaForm
from .models import India


def india_info(request):
    template_name = "curd_app/india_info.html"
    form = IndiaForm()
    if request.method == "POST":
        form = IndiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = India.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = India.objects.get(id=pk)
    form = IndiaForm(instance=obj)
    if request.method == "POST":
        form = IndiaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = 'curd_app/india_info.html'
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = India.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/confirm.html')

