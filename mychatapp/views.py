from django.shortcuts import render
from .models import Room,Message,User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create(username=username, password=password, email= email)
        if (user):
            return render(request, 'mychatapp/login.html')
        return render(request, "mychatapp/register.html", {'error_message': 'create user error'})
    return render(request, 'mychatapp/register.html')
    return render(request, "mychatapp/register.html", context)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username, password=password)
        if (user):
            rooms=Room.objects.all()
            context = {
                "user" : user,
                "rooms":rooms
            }
            return render(request, 'mychatapp/rooms.html', context)
        return render(request, "mychatapp/login.html", {'error_message': 'Invalid username or password'})
    return render(request, 'mychatapp/login.html')
def rooms(request):
    rooms=Room.objects.all()
    return render(request, "mychatapp/rooms.html",{"rooms":rooms})
