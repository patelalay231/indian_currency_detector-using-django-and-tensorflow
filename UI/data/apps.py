from django.apps import AppConfig
from django.contrib import admin
from .models import Data


class DataConfig(AppConfig):
    name = 'data'


admin.site.register(Data)