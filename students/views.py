from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Student
from .serialize import StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'id'
