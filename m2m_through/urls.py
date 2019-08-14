"""m2m_through URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, reverse_lazy
from .views import *


urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
        ),
    path(
        '',
        HomeView.as_view(),
        name='home'
        ),
    path(
        'submissions', 
        SubmissionList.as_view(), 
        name='list_submissions'
        ),
    path(
        'submissions/create',
        SubmissionCreate.as_view(
            success_url=reverse_lazy('list_submissions')
            ),
        name='create_submission'
    ),
    path(
        'submissions/<int:pk>',
        SubmissionDetail.as_view(),
        name="submission_detail"
    ),
    path(
        'submissions/update/<int:pk>',    
        SubmissionUpdate.as_view(),
        name="update_submission"
    ),
    path(
        'submissions/delete/<int:pk>',
        SubmissionDelete.as_view(
            success_url=reverse_lazy('list_submissions')
            ),
        name="delete_submission"
    ),
    path(
        'publishers', 
        PublisherList.as_view(), 
        name='list_publishers'
        ),
    path(
        'publishers/create',
        PublisherCreate.as_view(
            success_url=reverse_lazy('list_publishers')
            ),
        name='create_publisher'
    ),
    path(
        'publishers/<int:pk>',
        PublisherDetail.as_view(),
        name="publisher_detail"
    ),
    path(
        'publishers/update/<int:pk>',    
        PublisherUpdate.as_view(),
        name="update_publisher"
    ),
    path(
        'publishers/delete/<int:pk>',
        PublisherDelete.as_view(
            success_url=reverse_lazy('list_publishers')
            ),
        name="delete_publisher"
    ),
]
