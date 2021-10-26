from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectsList=[
    {
        'id':'1',
        'title':'E-Commerce Website',
        'description':"this is an e-commerce website"
    },
        {
        'id':'2',
        'title':'portfolio Website',
        'description':"this is an portfolio website"
    },
        {
        'id':'3',
        'title':'Social Network',
        'description':"this is an Social Network"
    }
]
def projects(request):
    context = {'projects':projectsList}
    return render(request, 'projects/projects.html',context)


def project(request, pk):

    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html',{"project":projectObj})
