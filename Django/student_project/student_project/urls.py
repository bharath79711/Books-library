"""
URL configuration for student_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
# from st.views import *
from django.contrib import admin
from django.urls import path,include

from StudApp.views import Studentsview, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Studentsview.as_view(),name='home_url'),
    path('list',StudentListView.as_view(),name='list_url'),
    path('detail/<int:pk>',StudentDetailView.as_view(),name='detail_url'),
    path('create',StudentCreateView.as_view(),name='create_url'),
    path('update/<int:pk>',StudentUpdateView.as_view(),name='update_url'),
    path('delete/<int:pk>',StudentDeleteView.as_view(),name='delete_url'),











    # path('', include('school.urls')),
    # path('', HomeView.as_view(), name='home'),
    # path('list/', StudentListView.as_view(), name='list'),
    # path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    # path('create/', StudentCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]
