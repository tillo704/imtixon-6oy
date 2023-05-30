from django.shortcuts import render,get_object_or_404
from .models import Customer,Reservation,Ticket
from rest_framework import decorators
from .serializer import ReservationSerializer,CustomerSerializer,TicketSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated



class CustomListCreatAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Customer.objects.all()
    serializer_class= CustomerSerializer
    lookup_field = 'pk' 


class CustomerRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'
    

class ReservationListCreatAPIView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk'


class ReservationsRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'  

class TicketListCreatAPIView(ListCreateAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'pk'

class TicketRetriveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'pk'





