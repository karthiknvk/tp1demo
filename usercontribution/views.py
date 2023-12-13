from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addreview(request):
  return HttpResponse("ADD REVIEW")

@login_required
def addspot(request):
  return HttpResponse("ADD SPOT")

def showreview(request):
  pass