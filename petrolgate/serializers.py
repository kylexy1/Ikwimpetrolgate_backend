from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import Data,Info

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    header_total = serializers.CharField(required=False, allow_blank=True, max_length=100)
    header_revenue = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_bon = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_cards = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_discounts = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_stock = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_cards_sold = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_bon_sold = serializers.CharField(required=False, allow_blank=True, max_length=100)
    right_cards_in_stock = serializers.CharField(required=False, allow_blank=True, max_length=100)


    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Data.objects.create(**validated_data)


class InfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    tin_number = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=100)
    district = serializers.CharField(required=False, allow_blank=True, max_length=100)
    sector = serializers.CharField(required=False, allow_blank=True, max_length=100)


    

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Info.objects.create(**validated_data)


    