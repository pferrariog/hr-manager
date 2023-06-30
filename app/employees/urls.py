from django.urls import path

from .views import EditEmployee
from .views import ListEmployees


urlpatterns = [
    path("", ListEmployees.as_view(), name="employees_information"),
    path("edit/<int:id>/", EditEmployee.as_view(), name="edit_employee"),
]
