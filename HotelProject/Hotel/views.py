from django.shortcuts import render,get_object_or_404,redirect
from .models import Room, Booking
from .forms import BookingForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# bookings/views.py


def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

def room_details(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'hotel/room_details.html', {'room': room})

#Registration view

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'hotel/register.html', {'form': form})


#Booking view

@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(request,'Room booked successfully!')
            return redirect('room_list')
    else:
        form = BookingForm()
    return render(request, 'hotel/book_room.html', {'form': form})