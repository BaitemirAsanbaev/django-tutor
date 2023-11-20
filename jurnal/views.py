from django.shortcuts import render, redirect
from .models import Jurnal
from .form import JurnalForms

def home_page(request):
    jurnal = Jurnal.objects.all()
    return render(request, 'index.html', {'data':jurnal})

def create_jurnal(request):
    form = JurnalForms
    if request.method == 'POST':
        form = JurnalForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})

def update_jurnal(request, id):
    form = JurnalForms
    jurnal = Jurnal.objects.get(id=id)

    if request.method == 'POST':
        form = JurnalForms(request.POST, request.FILES, instance=jurnal)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {"form": form})


def delete_jurnal(request, id):
    jurnal = Jurnal.objects.get(id=id)
    if request.method == 'POST':
        jurnal.delete()
        return redirect('home')
    return render(request, 'delete.html', {'jurnal': jurnal})