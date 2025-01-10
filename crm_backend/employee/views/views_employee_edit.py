from django.shortcuts import render, get_object_or_404, redirect
from ..models import Employee
from django.utils.dateparse import parse_date

def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.department = request.POST.get('department')
        employee.position = request.POST.get('position')
        employee.id_card_number = request.POST.get('id_card_number')
        employee.gender = request.POST.get('gender')
        employee.age = request.POST.get('age') or None
        employee.phone_number = request.POST.get('phone_number')
        employee.education = request.POST.get('education')
        employee.native_place = request.POST.get('native_place')
        employee.marital_status = request.POST.get('marital_status')
        employee.entry_date = parse_date(request.POST.get('entry_date')) or None
        employee.seniority_days = request.POST.get('seniority_days') or None
        employee.current_address = request.POST.get('current_address')
        employee.labor_contract_type = request.POST.get('labor_contract_type')
        employee.contract_start_date = parse_date(request.POST.get('contract_start_date')) or None
        employee.contract_end_date = parse_date(request.POST.get('contract_end_date')) or None
        employee.status = request.POST.get('status')
        employee.last_working_day = parse_date(request.POST.get('last_working_day')) or None
        employee.resignation_reason = request.POST.get('resignation_reason')
        employee.save()
        return redirect('employee:employee_list')
    return render(request, 'employee/employee_edit.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee:employee_list')