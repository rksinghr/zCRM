from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LeadForm
from .models import Lead

def leads_list(request):
    if request.user.is_authenticated:
        records = Lead.objects.all()

        return render(request, 'lead/show_records.html', {'records':records})
    else:
        messages.success(request, "Login Required!")
        return redirect('home')

def view_lead(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Lead.objects.get(id=pk)
		return render(request, 'lead/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Login Required!")
		return redirect('home')

def delete_lead(request, pk):
	if request.user.is_authenticated:
		delete_it = Lead.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "Login required!")
		return redirect('home')

def add_lead(request):
    form = LeadForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                var_user = request.user

                record = Lead(
                    name = request.POST.get('name'),
                    status = request.POST.get('status'),
                    phone = request.POST.get('phone'),
                    lastContact = request.POST.get('lastContact'),
                    contact = request.POST.get('contact'),
                    assignedTo = request.POST.get('assignedTo'),
                )
                record.save()
                
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'lead/add_record.html', {'form':form})
    else:
        messages.success(request, "Login required!")
        return redirect('home')

def update_lead(request, pk):
	if request.user.is_authenticated:
		current_record = Lead.objects.get(id=pk)
		form = LeadForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'lead/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
