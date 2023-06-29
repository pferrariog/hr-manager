from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    """Access index homepage method"""
    data = {"user": request.user}
    return render(request, "core/index.html", data)
