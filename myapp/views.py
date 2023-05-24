# views.py
from django.shortcuts import render, redirect
from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,
                              redirect)
from .models import *
from .forms import *
from django.db.models import Q

def login_view(request):
    employees = Employee.objects.all()[:300] 
    count_all = Employee.objects.all().count()
    count_complete = Employee.objects.filter(proj_stat="Complete").count()
    count_ongoing = Employee.objects.filter(proj_stat="On-Going").count()
    count_procurement = Employee.objects.filter(proj_stat="Under Procurement").count()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'dashboard.html', {'error_message': error_message, 'employees':employees, 'count_all':count_all, 'count_complete':count_complete, 'count_ongoing':count_ongoing, 'count_procurement':count_procurement})



@login_required

def logout_view(request):
    logout(request)     
    return redirect('/')



def addnew(request):
    context = {}
 
    # add the dictionary during initialization
    form = NewEmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "add_record.html", context)


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(desc__icontains=q) | Q(loc__icontains=q) | Q(proj_stat__icontains=q))
        employees = Employee.objects.filter(multiple_q)
    else:
        employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'project_table.html', context)

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    form = NewEmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/caap_ap")  
    return render(request,'edit.html', {'employee':employee})  



def show_project(request, id): 
    context ={}

    context["project"] = Employee.objects.get(id = id)
          
    return render(request, "show_project.html", context)

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = NewEmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/caap_ap")  
    return render(request, 'edit.html', {'employee': employee})  


def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/") 


def infoView(request):
    return render(request,'info.html')

def viewProject(request,id):

    view_proj = Employee.objects.get(id = id)

    
        # green
    if view_proj.progress >= 90 and view_proj.progress <= 100:
        progress_color = "#5FD068"
        # blue
    if  view_proj.progress >= 75 and view_proj.progress <= 89:        
        progress_color = "#62CDFF"
        # yello
    if  view_proj.progress >= 30 and view_proj.progress <= 74:
        progress_color = "#FFE15D"
        # red
    if  view_proj.progress >= 0 and view_proj.progress <= 29:
        progress_color = "#FD8A8A"
    
    return render(request,'view.html', {'progress_color': progress_color, 'view' : view_proj })

def showView(request,id):
    context = {}
    context["proj_detail"] = Employee.objects.get(id=id)
    return render(request,'show.html')


def dashView(request):
    employees = Employee.objects.all()[:300] 
    count_all = Employee.objects.all().count()
    count_complete = Employee.objects.filter(proj_stat="Complete").count()
    count_ongoing = Employee.objects.filter(proj_stat="On-Going").count()
    count_procurement = Employee.objects.filter(proj_stat="Under Procurement").count()
    return render(request,"dashboard.html",{'employees':employees, 'count_all':count_all, 'count_complete':count_complete, 'count_ongoing':count_ongoing, 'count_procurement':count_procurement})

def complete_projects(request):
    complete = Employee.objects.filter(proj_stat='Complete').all()

    return render(request,'myapp/status/complete_projects.html', {'complete': complete})

def ongoing_projects(request):
    ongoing = Employee.objects.filter(proj_stat='On-Going').all()

    return render(request,'myapp/status/ongoing_projects.html', {'ongoing': ongoing})


def procurement_projects(request):
    procurement = Employee.objects.filter(proj_stat='Under Procurement').all()

    return render(request,'myapp/status/procurement_projects.html', {'procurement': procurement})

def progress_view(request):
    # Calculate the progress as a percentage of the target number of signups
    total_capacity = 100  # Replace with your own target number
    users = 31
    comp_projects = Employee.objects.filter(proj_stat='Complete').count()
    ongoing_projects = Employee.objects.filter(proj_stat='On-Going').count()
    proc_projects = Employee.objects.filter(proj_stat='Under Procurement').count()
    progress_cp = comp_projects / total_capacity * 100 
    # * 100 is a conversion of int to float
    progress_og = ongoing_projects / total_capacity * 100
    progress_proc = proc_projects / total_capacity * 100
    high = 'green'
    medium = 'orange'
    low = 'red'
    if progress_cp < 30:
        progress_color = low
    elif progress_cp < 80:
        progress_color = medium

    else:
        progress_color = high

    # Render a template that displays the progress bar
    context = {
        'progress_color': progress_color,
        'progress_cp':progress_cp,
        'progress_og':progress_og,
        'progress_proc':progress_proc,
    }

    return render(request, 'sample.html', context)





