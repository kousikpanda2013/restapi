from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from django.db.models import Q
# Create your views here.


class UserRetrieveCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(company__icontains=query) |
                Q(age__icontains=query) |
                Q(state__icontains=query) |
                Q(pin__icontains=query) |
                Q(email__icontains=query) |
                Q(web__icontains=query)
            )
        return queryset


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
