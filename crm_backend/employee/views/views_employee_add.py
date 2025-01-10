from django.shortcuts import render, redirect
from ..models import Employee

def add_employee(request):
    if request.method == "POST":
        try:
            Employee.objects.create(
                name=request.POST["name"],
                department=request.POST["department"],
                position=request.POST["position"],
                id_card_number=request.POST["id_card_number"],
                gender=request.POST["gender"],
                age=request.POST.get("age"),
                phone_number=request.POST.get("phone_number"),
                education=request.POST.get("education"),
                native_place=request.POST.get("native_place"),
                marital_status=request.POST.get("marital_status"),
                entry_date=request.POST.get("entry_date"),
                seniority_days=request.POST.get("seniority_days"),
                current_address=request.POST.get("current_address"),
                labor_contract_type=request.POST.get("labor_contract_type"),
                contract_start_date=request.POST.get("contract_start_date"),
                contract_end_date=request.POST.get("contract_end_date"),
                status=request.POST.get("status"),
                last_working_day=request.POST.get("last_working_day"),
                resignation_reason=request.POST.get("resignation_reason"),
            )
            return redirect("employee:employee_list")
        except Exception as e:
            return render(request, "employee/employee_add.html", {"error": str(e)})

    return render(request, "employee/employee_add.html")