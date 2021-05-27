from django.shortcuts import render
from user.models import *
from django.db.models import Q

# Create your views here.
def register(request):
    res=Customer.objects.filter(id__gte=4)
    return render(request,"register.html",{'res':res})
