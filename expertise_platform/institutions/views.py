from django.shortcuts import render, get_object_or_404,redirect
from .models import Institution, Requirement


def institution_list(request):
    query = request.GET.get('q')
    if query:
        institutions = Institution.objects.filter(name__icontains=query)
    else:
        institutions = Institution.objects.all()

    return render(request, 'institutions/institution_list.html', {'institutions': institutions})


def institution_profile(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    requirements = institution.requirements.all()
    return render(request, 'institutions/institution_profile.html', {'institution': institution, 'requirements': requirements})

def post_requirement(request, pk):
    institution = get_object_or_404(Institution, pk=pk)
    if request.method == 'POST':
        description = request.POST['description']
        Requirement.objects.create(institution=institution, description=description)
        return redirect('institution_profile', pk=institution.pk)
    return render(request, 'institutions/post_requirement.html', {'institution': institution})
