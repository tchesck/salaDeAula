from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from professor.models import Professor
from professor.serializers import ProfessorSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProfessorViewsSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProfessorSerializer
    # authentication_class = (TokenAuthentication,)
