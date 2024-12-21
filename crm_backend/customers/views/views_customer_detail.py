from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Customer


@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer.objects.prefetch_related('recordings', 'comments'), id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})