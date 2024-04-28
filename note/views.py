from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NoteForm
from .models import Note

def note_list(request):
    if request.user.is_authenticated:
        records = Note.objects.all()

        return render(request, 'note/show_records.html', {'records':records})
    else:
        messages.success(request, "Login Required!")
        return redirect('home')

def view_note(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Note.objects.get(id=pk)
		return render(request, 'note/record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Login Required!")
		return redirect('home')

def delete_note(request, pk):
	if request.user.is_authenticated:
		delete_it = Note.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully!")
		return redirect('home')
	else:
		messages.success(request, "Login required!")
		return redirect('home')

def add_note(request):
    form = NoteForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                var_user = request.user

                record = Note(
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
        return render(request, 'note/add_record.html', {'form':form})
    else:
        messages.success(request, "Login required!")
        return redirect('home')

def update_note(request, pk):
	if request.user.is_authenticated:
		current_record = Note.objects.get(id=pk)
		form = NoteForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'note/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
