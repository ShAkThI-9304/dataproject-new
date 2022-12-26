from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# Create your views here.

def home(request):
    return render(request,"bankinginfo/home.html")

@login_required(login_url='../accounts/login/')
def staff(request):
    return render(request,"bankinginfo/staff.html")

@permission_required('bankinginfo.view_staff',login_url='../accounts/login/')
def income(request):
    return render(request,"bankinginfo/income.html")


