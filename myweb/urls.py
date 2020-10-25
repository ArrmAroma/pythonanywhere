from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.Contact, name='contact'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    #path('upload',views.Upload, name='upload'),
    path('pageAdmin', views.PageAdmin, name='pageAdmin'),
    path('show', views.show, name="show"),
    #path('register', views.Register, name='register'),
]
