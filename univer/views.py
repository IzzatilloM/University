from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from univer.models import *


def home_view(request):
    return render(request,'index.html')

def yunalish_view(request):
    yunalish = Yunalish.objects.all()
    if request.method == 'POST':
        Yunalish.objects.create(
            nom=request.get.POST('nom'),
            aktiv=True if request.POST.get('aktiv') else request.POST.get('aktiv'))
        return redirect('/yunalish/')
    context = {
        'yunalish':yunalish,
    }
    return render(request,'yunalish.html',context)

def ustozlar_view(request):
    ustozlar = Ustoz.objects.all()
    context = {
        'ustozlar':ustozlar,
    }
    return render(request,'ustozlar.html',context)

def fanlar_view(request):
    fanlar = Fan.objects.all()
    yunalishlar = Yunalish.objects.order_by('nom')
    if request.method == 'POST':
        Fan.objects.create(
        nom=request.POST.get('nom'),
        asosiy=True if request.POST.get('asosiy') else request.Post.get('asosiy'),
        yunalish=Yunalish.objects.get(id=request.POST.get('yunalish_id')))
        return redirect('/fanlar/')
    context = {
        'fanlar':fanlar,
        'yunalishlar':yunalishlar,
    }
    return render(request,'fanlar.html',context)

def yunalish_confirm_delete_view(request,pk):
    yunalish  = get_object_or_404(Yunalish,pk=pk)
    context = {
        'yunalish':yunalish,
    }
    return render(request,'yunalish_confirm_delete.html',context)

def yunalish_delete_view(request,pk):
    yunalish = get_object_or_404(Yunalish,pk=pk)
    yunalish.delete()
    return redirect('/yunalish/')

def fanlar_delete_view(request,pk):
    fanlar = get_object_or_404(Fan,pk=pk)
    fanlar.delete()
    return redirect('/fanlar/')