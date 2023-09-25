from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeForm




class EmployeeListView(ListView):
    template_name="employee_list.html"
    model=Employee
    context_object_name="employees"


    
class EmployeeDetailView(DetailView):
    template_name="employee_list.html"
    model=Employee
    context_object_name="employee"


class EmployeeCreateView(CreateView):
    form_class=EmployeeForm
    model=Employee
    template_name="employee_add.html"
    success_url=reverse_lazy("employee_add")

    def form_valid(self, form):
        
        
        messages.success(self.request,"employee has been created")
        return super().form_valid(form)


    
class  EmployeeUpdateView(UpdateView):
        model=Employee
        form_class=EmployeeForm
        template_name="employee_edit.html"
        success_url=reverse_lazy("employee_list")

        def form_valid(self, form):
            messages.success(self.request,"changed")
            return super().form_valid(form)



def employee_delete_view(request,*args,**kargs):
    id=kargs.get("pk")
    Employee.objects.get(id=id).delete()
    messages.success(request,"employee removed")
    return redirect("employee_list")