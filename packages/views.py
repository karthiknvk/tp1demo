from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Set1,Set2,Set3,Set4
# Create your views here.

def logout(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')

@login_required
def home(request):
  if request.method=="POST":
    return packageview(request)
    if 'budget' in request.POST:
      return budgetview(request)
    elif 'destination' in request.POST:
      return destinationview(request)
  else:
    pricelist=['under 5000','5000-10000','10000-15000','above 15000']
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"home.html",{'pricelist':pricelist,'destinationlist':destinationlist})
  



def packageview(request):
  packagelist1=Set1.objects.all
  return render(request,'tourpackages.html',{'packagelist1':packagelist1})

