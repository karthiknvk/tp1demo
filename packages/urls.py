from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.prefer,name='prefer'),#root url
  path('budgetview',views.budgetview,name='budgetview'),#budgetview=is path given in url,name=budgetviewpackages=is name used to refer it in other places
  path('destinationview',views.destinationview,name='destinationview'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)