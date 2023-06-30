from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import *


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'
        # fields = ('name', 'contact_no',  )
        
class Product_InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Inquiry
        fields = '__all__'
        

