from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework import status, viewsets
from main_page.models import Subject
from main_page.serializers import SubjectSerializer
from .paginations import SubjectAPIPagination


# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    paginate_by = 2
    pagination_class = SubjectAPIPagination