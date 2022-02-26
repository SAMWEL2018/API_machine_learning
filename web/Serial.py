from rest_framework import serializers
from .models import comments

class Serializers(serializers.ModelSerializer):
    class Meta:
        model= comments
        fields=['email','message','is_positive']