from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session 
from django.core.mail import send_mass_mail
from django.core.mail import BadHeaderError, send_mail
# from user import utils
from django.views.generic import ListView, DetailView, TemplateView ,View
import os
import io
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mass_mail
from django.core.mail import BadHeaderError, send_mail
from datetime import timedelta, date
import datetime

from django.core.files.base import ContentFile
import base64
# Create your views here.
from django.http import HttpResponse, JsonResponse ,HttpResponseBadRequest
from rest_framework import status
from .serializers import *
from .models import *
import requests
import json

from rest_framework.decorators import api_view
# from account.models import Account
from allauth.account import *
from rest_framework.authentication import TokenAuthentication
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics, permissions
from knox.models import AuthToken

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination



class API_Inquiry(APIView):
    def post(self, request):
        serializer = InquirySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class API_Product_Inquiry(APIView):
    def post(self, request):
        serializer = Product_InquirySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

