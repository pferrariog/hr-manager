from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets

from .serializers import UserSerializer


@login_required
def index(request):
    """Access index homepage method"""
    data = {"user": request.user}
    return render(request, "core/index.html", data)


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited"""

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
