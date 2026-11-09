from rest_framework import serializers
from .models import Student





class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'course', 'is_active']

# GET /api/students/
# POST /api/students/
# PUT /api/students/{id}/
# DELETE /api/students/{id}/
# PATCH /api/students/{id}/

