from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    return render(request,'login.html')

def make(request):
    return render(request,'make.html')

def option(request):
    return render(request,'option.html')

def create(request):
    
    return redirect('/')

def destroy(request, room_id):
    return redirect('/')