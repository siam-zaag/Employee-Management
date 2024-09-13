from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.core.paginator import Paginator

# def employee_list(request):
#     search_query = request.GET.get('search', '')
#     employees = Employee.objects.filter(first_name__icontains=search_query) | Employee.objects.filter(email__icontains=search_query)
    
#     paginator = Paginator(employees, 10)  # Show 10 employees per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'employees/employee_list.html', {'page_obj': page_obj, 'search_query': search_query})
def employee_list(request):
    # Fetch search query from the GET request
    search_query = request.GET.get('search', '')  # Get search term from the request (default is an empty string)
    
    # Filter employees based on the search query (case-insensitive search on 'first_name' and 'email')
    employees = Employee.objects.filter(first_name__icontains=search_query) | Employee.objects.filter(email__icontains=search_query)

    # Continue with pagination setup
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {'page_obj': page_obj, 'search_query': search_query})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_or_edit_employee.html', {'form': form})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/add_or_edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/delete_employee_confirm.html', {'employee': employee})
