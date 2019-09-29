from django.shortcuts import render
from .models import Gonderi

def gonderiListele(request):
    gonderiler = Gonderi.objects.all()
    return render(request,'EdzBlog/GonderiListe.html',{'gonderiler':gonderiler})