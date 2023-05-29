from django.urls import path
from .views import CustomListCreatAPIView,CustomerRetriveUpdateDeleteAPIView,TicketListCreatAPIView,TicketRetriveUpdateDeleteAPIView,ReservationListCreatAPIView,ReservationsRetriveUpdateDeleteAPIView

urlpatterns = [
    path('customer/',CustomListCreatAPIView.as_view(), name='custon-list-creat-view'),
    path('customer/<int:pk>/',CustomerRetriveUpdateDeleteAPIView.as_view(),name='cat-deatil-view'),
    path('ticket/',TicketListCreatAPIView.as_view(), name='tiket-list-creat-view'),
    path('ticket/<int:pk>/',TicketRetriveUpdateDeleteAPIView.as_view(),name='ticket-deatil-view'),
    path('register/',ReservationListCreatAPIView.as_view(), name='register-list-creat-view'),
    path('register/<int:pk>/',ReservationsRetriveUpdateDeleteAPIView.as_view(),name='register-deatil-view'),




]