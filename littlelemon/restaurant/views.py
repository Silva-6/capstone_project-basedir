from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    DestroyAPIView
)
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def index(request):
    return render(request, 'index.html', {})