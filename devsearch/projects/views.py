from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# fetching and sending all projects to template
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


# get one sepecific project
def project(request, pk):

    project = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {"project": project})

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={"form":form}
    return render(request,'projects/create-project.html',context)


def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {"form":form}
    return render(request, 'projects/create-project.html',context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object":project}
    return render(request, 'projects/delete_object.html',context)