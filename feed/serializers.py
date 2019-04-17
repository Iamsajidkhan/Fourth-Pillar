from rest_framework import serializers
from .models import Republic, Ndtv, Zeenews, Indiatoday


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Republic
        fields = ('headline','link')
