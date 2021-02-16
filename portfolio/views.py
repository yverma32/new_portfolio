from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Project, Myskill, Contact
# Create your views here.

def index(request):

    projects = Project.objects
    skills = Myskill.objects.all()
    n = skills.count()
    if n%2==0:
        n = n/2
    else:
        n = (n+1)/2
    m = skills.count() - n

    skills1 = skills[:n]
    skills2 = skills[n:n+m]

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'skills1':skills1,
        'skills2':skills2,
    })


def thanks(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return render(request, 'portfolio/thanks.html')



def details(request, project_id):
    detailpage = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/details.html', {
        'details': detailpage,
    })
