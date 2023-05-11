from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from projects.models import Project, Review, Tag
from users.models import Profile, Skill, Message

admin_check = user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
redactor_check = user_passes_test(lambda user: user.groups.filter(name='Redactor').exists())


@admin_check
def admin_dashboard(request):
    users = User.objects.all()
    projects = Project.objects.all()
    context = {'users': users, 'projects': projects}
    return render(request, 'management/admin_dashboard.html', context)


@redactor_check
def redactor_dashboard(request):
    users = User.objects.all()
    projects = Project.objects.all()
    context = {'users': users, 'projects': projects}
    return render(request, 'management/redactor_dashboard.html', context)
