from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn python'}
    {'id': 2, 'name': 'Lets learn python'}
    {'id': 3, 'name': 'Lets learn python'}


]


def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')

# Create your views here.
