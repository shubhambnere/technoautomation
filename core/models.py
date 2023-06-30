from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import os
# from .utils import id_generator, id_generator_custom
import uuid
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.http import JsonResponse

from importlib import import_module
from datetime import datetime, timedelta

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

import random
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
# from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import gettext_lazy as _

uuid.uuid4().hex[:6].upper()

state_choices           = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("Delhi","Delhi"),("Puducherry","Puducherry"),("Other","Other"))

class Inquiry(models.Model):
    name                 = models.CharField(max_length=30)
    contact_no           = models.CharField(max_length=12)
    email                = models.EmailField(max_length=254)
    message              = models.TextField(max_length=10000)
    
    created_on                  = models.DateTimeField(auto_now_add=True)
    updated_on                  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  str(self.id) + " "  + str(self.name)

    def save(self,*args, **kwargs):
        super(Inquiry, self).save()
        return self

    class Meta: 
        ordering = ['-created_on']


class Product_Inquiry(models.Model):
    product              = models.CharField(max_length=30)
    name                 = models.CharField(max_length=30)
    contact_no           = models.CharField(max_length=12)
    email                = models.EmailField(max_length=254)
    message              = models.TextField(max_length=10000)
    
    created_on                  = models.DateTimeField(auto_now_add=True)
    updated_on                  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  str(self.id) + " "  + str(self.name)

    def save(self,*args, **kwargs):
        super(Product_Inquiry, self).save()
        return self

    class Meta: 
        ordering = ['-created_on']
