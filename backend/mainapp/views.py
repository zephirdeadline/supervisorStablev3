from django.shortcuts import render

# Create your views here.
from djangoAPI_rest_object.djangoapi_rest_object.rest_object.views import action
from mainapp.models import Student, Horse
from mainapp.serializers.horseSerialiazer import HorseSerializer
from mainapp.serializers.studentSerializer import StudentSerializer


def student(request, id_obj=None):
    return action(request, Student, StudentSerializer, id_obj)


def horse(request, id_obj=None):
    return action(request, Horse, HorseSerializer, id_obj)
