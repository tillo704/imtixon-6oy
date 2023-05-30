from rest_framework import serializers
from .models import Customer,Reservation,Ticket



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ('id', )

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ('id',)
    

class ReservationSerializer(serializers.ModelSerializer):
    cust_id = CustomerSerializer()   
    ticket = TicketSerializer()
    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ('id',)
    

