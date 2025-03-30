from rest_framework import serializers
from .models import Grade_Calc

class Grade_Calc_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade_Calc
        fields = ('id','input_file','input_data')