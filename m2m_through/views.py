from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  )
from .models import *


class HomeView(TemplateView):
    template_name = 'index.html'
    

class SubmissionList(ListView):
    model = Submission
    context_object_name = 'submissions'


class SubmissionCreate(CreateView):
    model = Submission
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/'


class SubmissionDetail(DetailView):
    model = Submission


class SubmissionUpdate(UpdateView):
    model = Submission
    fields = '__all__'
    template_name_suffix = '_update_form'


class SubmissionDelete(DeleteView):
    model = Submission
    

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'


class PublisherCreate(CreateView):
    model = Publisher
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/'


class PublisherDetail(DetailView):
    model = Publisher


class PublisherUpdate(UpdateView):
    model = Publisher
    fields = '__all__'
    template_name_suffiex = '_update_form'


class PublisherDelete(DeleteView):
    model = Publisher
