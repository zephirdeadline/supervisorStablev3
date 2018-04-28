from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from django.db import models

from mainapp.models import Horse


class HorseSerializer(serializers.ModelSerializer):
    #tags = TagSerializer(many=True)
    id = models.IntegerField(default=1)

    class Meta:
        model = Horse
        fields = ('id', 'name')

    def update(self, instance, validated_data):
        self.creator(instance, validated_data)
        instance.save()
        return instance

    def create(self, validated_data, user=None):
        r = Horse()
        r.user = user
        self.creator(r, validated_data)
        r.save()
        return r

    def creator(self, instance, validated_data):
        instance.name = validated_data.get('name')
        return instance
