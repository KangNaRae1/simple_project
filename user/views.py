from django.shortcuts import render,redirect,get_object_or_404
from .models import room, user_choice

# Create your views here.
def rooms(request):
    rooms=room.objects
    room_list=room.objects.all()
    return render(request,'rooms.html',{'rooms':rooms})

def room_detail(request,room_id):
    room_detail=get_object_or_404(room,pk=room_id)
    return render(request, 'room_detail.html')

def name(request):
    return render(request,'name.html')

def result(request):
    user_choice.user_name=request.GET['username']
    return render(request,'result.html')

def main(request):
    return render(request,'main.html')

