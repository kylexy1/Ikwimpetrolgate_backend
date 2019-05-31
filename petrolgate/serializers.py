from django.contrib.auth.models import User, Group
from rest_framework import serializers

class Task(object):
    def __init__(self, **kwargs):
        for field in ('header', 'right'):
            setattr(self, field, kwargs.get(field, None))





class HeaderSerializer(serializers.Serializer):
	total = serializers.CharField()
	revenue = serializers.CharField()
	growth = serializers.CharField()


class RightSerializer(serializers.Serializer):
	bon = serializers.CharField()
	cards = serializers.CharField()
	discounts = serializers.CharField()
	stock = serializers.CharField()
	cardsSold = serializers.CharField()
	bonSold = serializers.CharField()
	cardsInStock = serializers.CharField()
		


class TaskSerializer(serializers.Serializer):
    header = HeaderSerializer(many = True)
    right = RightSerializer(many = True)
   
   
 