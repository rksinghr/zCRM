from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CompanyForm
from .models import Company

def list_records(request):
    if request.user.is_authenticated:
        records = Company.objects.all()

        return render(request, 'company/show_records.html', {'records':records})
    else:
        messages.success(request, "Login Required!")
        return redirect('home')

def view_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Company.objects.get(id=pk)
		return render(request, 'company/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Login Required!")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Company.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "Login required!")
		return redirect('home')

def add_record(request):
    form = CompanyForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                var_user = request.user

                record = Company(
                    name = request.POST.get('name'),
                    industry = request.POST.get('industry'),
                    email = request.POST.get('email'),
                    phone = request.POST.get('phone'),
                    website = request.POST.get('website'),
                    address1 = request.POST.get('address1'),
                    address2 = request.POST.get('address2'),
                    city = request.POST.get('city'),
                    state = request.POST.get('state'),
                )
                record.save()
                
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'company/add_record.html', {'form':form})
    else:
        messages.success(request, "Login required!")
        return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Company.objects.get(id=pk)
		form = CompanyForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'company/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
