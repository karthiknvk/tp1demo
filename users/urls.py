from django.urls import path,include
from . import views
#from packages.views import prefer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.index,name='index'),#root url
  path('signup',views.signup,name='signup'),
  path('login',views.login,name='login'),
  path('packages/',include('packages.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)