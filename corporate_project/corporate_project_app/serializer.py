#importing necessary modules
from rest_framework import serializers
from .models import Company,Employee,Project

#making a serializer for the company model for all fields
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='_all_'

#making a serializer for the employee model for all fields
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='_all_'


#making a serializer for the project model for all fields
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='_all_'
