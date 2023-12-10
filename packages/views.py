from django.shortcuts import render
from .models import Set1,Set2,Set3,Set4
# Create your views here.


def prefer(request):
  if request.method=="POST":
    if 'budget' in request.POST:
      return budgetview(request)
    elif 'destination' in request.POST:
      return destinationview(request)
  else:
    pricelist=['under 5000','5000-10000','10000-15000','above 15000']
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"prefercopy.html",{'pricelist':pricelist,'destinationlist':destinationlist})
  



def budgetview(request):
  packagelist1=Set1.objects.all
  return render(request,'tourpackages.html',{'packagelist1':packagelist1})

def destinationview(request):
  pass