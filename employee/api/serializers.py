from rest_framework import serializers
from django.contrib.auth.models import User
from emphub.models import Employee,Project,Department,Position



class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model=Project
        fields=["name"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=["name"]

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Position
        fields=["title"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username"]

class EmployeeSearializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    project_name=ProjectSerializer(read_only=True,many=True)
    department_name=DepartmentSerializer(source='department',read_only=True)
    position_name=PositionSerializer(source='position',read_only=True)
    user_name=UserSerializer(source='user',read_only=True)
    class Meta:
        model=Employee
        exclude=("projects","department","position","user",)






