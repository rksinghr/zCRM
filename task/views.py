from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import pywhatkit
from django.contrib import messages
from .forms import TaskForm
from .models import Task

def task_list(request):
    if request.user.is_authenticated:
        records = Task.objects.all()

        return render(request, 'task/show_records.html', {'records':records})
    else:
        messages.success(request, "Login Required!")
        return redirect('home')

def view_task(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Task.objects.get(id=pk)
		return render(request, 'task/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Login Required!")
		return redirect('home')

def delete_task(request, pk):
	if request.user.is_authenticated:
		delete_it = Task.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "Login required!")
		return redirect('home')
def whatsapp(ph, msg):
    import time
    import webbrowser as wb
    import pyautogui as pg

    var_phone = "+91" + ph
    wb.open('https://web.whatsapp.com/send?phone='+var_phone+'&text='+msg)
    time.sleep(30)
    pg.press('enter')
    print("whatsapp msg sent")

def add_task(request):
    form = TaskForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                var_user = request.user
                var_related_to = form.cleaned_data['relatedTo']
                var_priority = form.cleaned_data['priority']
                var_status = form.cleaned_data['status']
                var_assigned = form.cleaned_data['assignedTo']

                record = Task(
                    name = request.POST.get('name'),
                    description = request.POST.get('description'),
                    dueDate = request.POST.get('dueDate'),
                    priority = var_priority,
                    status = var_status,
                    relatedTo = var_related_to,
                    assignedTo = var_assigned,
                    createdBy = var_user
                )
                record.save()
                ph = "8886588873"
                msg = "This is an automated message from MyCRM to notify you for a new Task assignment, good luck!"
                whatsapp(ph, msg)
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'task/add_record.html', {'form':form})
    else:
        messages.success(request, "Login required!")
        return redirect('home')

def update_task(request, pk):
	if request.user.is_authenticated:
		current_record = Task.objects.get(id=pk)
		form = TaskForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'task/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
