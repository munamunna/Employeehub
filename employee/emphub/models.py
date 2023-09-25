from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    employee_number=models.PositiveIntegerField()
    email = models.EmailField(unique=True) 
    mobile_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project)

    @property
    def project_name(self):
        return self.projects.all()
    
    @property
    def department_name(self):
        return self.department.all()
    
    @property
    def position_name(self):
        return self.department.all()
    
    @property
    def user_name(self):
        return self.department.all()
    
    def __str__(self):
        return self.first_name





# Create your models here.
