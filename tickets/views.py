from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ticketapi.serializers import UserSerializer, TicketSerializer, CategorySerializer , ChatSerializer
from django.contrib.auth.models import User
from tickets.models import Ticket, Category , Chat

# Create your views here.
from rest_framework.permissions import IsAuthenticated


       
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ChatViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
