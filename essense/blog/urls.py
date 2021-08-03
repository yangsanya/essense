from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', BlogHome.as_view(), name='blog_home'),
    path('blog/post/<slug:slug>', PostView.as_view(), name='post'),

]
