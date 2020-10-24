#from pythonanywhere.mysite.myweb.views import Contact
from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('show/', views.show),
    path('contact/', views.Contact),
    path('myweb/',include('myweb.urls')),
    path('login/', views.Login),
    path('logout/', views.Logout),
    path('pageAdmin/', views.PageAdmin),
    path('', views.home),
    path('admin/', admin.site.urls),
   # path('logout/', views.logout),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
