# employees/urls.py
from django.urls import path
from emphub import views

urlpatterns = [
    path('employees', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/change/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_change'),
    path('employees/remove/<int:pk>/', views.employee_delete_view, name='employee_remove'),
]
