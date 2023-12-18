from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
#from .models import Set1,Set2,Set3,Set4
from .models import Packageset
# Create your views here.

def logoutview(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')

@login_required
def accountview(request):
    user_profile=request.user
    return render(request,'accountdetails.html',{'user_profile':user_profile})

@login_required
def home(request):
  if request.method=="POST":
    return packageview(request)
    
  else:
    #pricelist=['under 5000','5000-10000','10000-15000','above 15000']
    daylist=[1,2,3,4,5,6,7]
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"home.html",{'daylist':daylist,'destinationlist':destinationlist})
  


'''
def packageview(request):
  budget=request.POST.get('budget')
  destination = request.POST.get('destination', '')

  if budget=='under 5000':
    packagelist=Set1.objects.all()
  elif budget=='5000-10000':
    packagelist=Set2.objects.all()
  elif budget=='10000-15000':
    packagelist=Set3.objects.all()
  elif budget=='above 15000':  
    packagelist=Set4.objects.all()
  
  return render(request,'tourpackages.html',{'packagelist':packagelist,'budget':budget})
  
'''  

def packageview(request):
  day=request.POST.get('day')
  destination = request.POST.get('destination', '')
  if destination:
     packagelist=Packageset.objects.filter(district=destination)
  else:
    packagelist=Packageset.objects.all()
  return render(request,'tourpackages.html',{'packagelist':packagelist,'day':day})

