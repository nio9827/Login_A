from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.logiarse,name='login'),
    path('registrar/',views.registrar,name='registrar'),
    path('success/',views.success,name='success'),
    path('logout/',views.logout_view,name='logout'),
]
