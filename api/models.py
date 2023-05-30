from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    cantact = models.CharField(max_length=25)
    email = models.EmailField() 



class Ticket(models.Model):
    ticket_num = models.PositiveBigIntegerField()
    date_avail = models.DateField()
    date_flight = models.DateField()
    time_depart = models.TimeField()
    time_land = models.TimeField()
    destination = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Ticket - {self.ticket_num}"



class Reservation(models.Model):
    
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    data_reserve = models.DateField()
    date_accom = models.DateField()

    def __str__(self) -> str:
        return self.admin








