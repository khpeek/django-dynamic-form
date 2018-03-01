"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import CheckInCreate, CheckInList, CheckInDetail, CheckInUpdate, get_checkin_type

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkins/new', CheckInCreate.as_view(), name='checkin-create'),
    path('checkins', CheckInList.as_view(), name='checkin-list'),
    path('checkins/<int:pk>', CheckInDetail.as_view(), name='checkin-detail'),
    path('checkins/<int:pk>/update', CheckInUpdate.as_view(), name='checkin-update'),
    path('get_checkin_type', get_checkin_type, name='get-checkin-type'),
]
