#from django.contrip import admin
from django.contrib import admin 
from .models import MyPicture, Question, Choice

admin.site.register(MyPicture)
admin.site.register(Question)
admin.site.register(Choice)

