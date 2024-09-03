from rest_framework import serializers
from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('__all__')


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['title']

    
class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['title', 'front_image']