from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.

def home(request):

    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user, 'user****')
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully loged in')
            return redirect('home')
        else:
            messages.success(request, 'there was an error in login')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records' : records})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out')
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer': customer})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=pk)
        customer.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.success(request, 'you mused be logged In')
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    print('form')
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                print('you here')
                messages.success(request, 'record added successfully')
                return redirect('home')

        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, 'you must be loggen in')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'you mused be logged In')
        return redirect('home')
