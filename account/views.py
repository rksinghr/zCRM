from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, ActivityTypeForm, PriorityForm, StageForm, StatusForm
from .models import ActivityType, Priority, Stage, Status

def home(request):
    user = request.user
    # records = Profile.objects.filter(user = user.id)
    # count = records.count()
    count = 1

    if request.method == 'POST':
        var_username = request.POST['username']
        var_password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=var_username, password=var_password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser :
                return render(request,'account/dashboardAdmin.html', {'User': user, 'Count': count})
            else:
                return render(request,'account/dashboardUser.html', {'User': user, 'Count': count})
        else:
            messages.success(request, "Error!, please try again.")
            return redirect('home')
    else:
        return render(request, 'account/home.html', {'User': "Guest", 'Count': count})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logout successfull!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Auth & login
            var_user = form.cleaned_data['username']
            var_pwd = form.cleaned_data['password1']
            user = authenticate(username=var_user, password=var_pwd)
            login(request, user)
            messages.success(request, "User registered successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'account/register.html', {'form':form})
    return render(request, 'account/register.html', {'form':form})

def switch_model(argument):
    switcher = {
        1: ActivityType,
        2: Priority,
        3: Stage,
        4: Status,
    }
    return switcher.get(argument, "nothing")

def switch_form(argument):
    switcher = {
        1: ActivityTypeForm,
        2: PriorityForm,
        3: StageForm,
        4: StatusForm,
    }
    return switcher.get(argument, "nothing")

def list_records(request, key):
    if request.user.is_authenticated:
        records = switch_model(key).objects.all()

        return render(request, 'account/show_records1.html', {'records':records, 'key':key})
    else:
        messages.success(request, "Login Required!")
        return redirect('home')

def view_record(request, key, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = switch_model(key).objects.get(id=pk)
		return render(request, 'account/record.html', {'customer_record':customer_record, 'key':key})
	else:
		messages.success(request, "Login Required!")
		return redirect('home')

def delete_record(request, key, pk):
	if request.user.is_authenticated:
		delete_it = switch_model(key).objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "Login required!")
		return redirect('home')

def add_record(request, key):
    form = switch_form(key)(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                var_user = request.user

                record = switch_model(key)(
                    name = request.POST.get('name'),
                    description = request.POST.get('description'),
                )
                record.save()
                
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'account/add_record.html', {'form':form})
    else:
        messages.success(request, "Login required!")
        return redirect('home')

def update_record(request, key, pk):
	if request.user.is_authenticated:
		current_record = switch_model(key).objects.get(id=pk)
		form = switch_form(key)(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'account/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
