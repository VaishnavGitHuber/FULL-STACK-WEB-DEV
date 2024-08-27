# staff/views.py
from django.shortcuts import render, get_object_or_404
from .models import Staff


def staff_list(request):
    query = request.GET.get('q')
    if query:
        staff = Staff.objects.filter(name__icontains=query)
    else:
        staff = Staff.objects.all()

    return render(request, 'staff/staff_list.html', {'staff': staff})

def staff_profile(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff/staff_profile.html', {'staff': staff})
