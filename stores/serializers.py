from rest_framework import serializers
from django.contrib.auth.models import User
from stores.models import Store


class NearbyStoreSerializer(serializers.ModelSerializer):
    fields = "__all__"

    class Meta:
        ordering = ["created_at"]
