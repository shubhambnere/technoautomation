
from django.urls import include, path
from rest_framework import routers
from .views import *

from knox import views as knox_views


urlpatterns = [

    # path('register/', RegisterAPI.as_view(), name='register'),
    # path('login/', LoginAPI.as_view(), name='login'),
    # path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
    path('inquiry/', API_Inquiry.as_view()),
    path('product_inquiry/', API_Product_Inquiry.as_view()),
    # path('feed/', AdminFeedbacks.as_view()),
    # path('feed/<id>/', AdminFeedbacks.as_view()), 
    # path('bike_service/', AdminBikeService.as_view()),
    # path('bike_service/<id>/', AdminBikeService.as_view()) , 

]