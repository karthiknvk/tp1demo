from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  path('',views.index,name='index'),#root url
  path('signup',views.signup,name='signup'),
  path('login',views.login,name='login'),
  path('prefer',views.prefer,name='prefer'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)