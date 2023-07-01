from django.urls import path

from .views import CreateEmployee
from .views import DeleteEmployee
from .views import EditEmployee
from .views import ListEmployees


urlpatterns = [
    path("", ListEmployees.as_view(), name="employees_information"),
    path("new/", CreateEmployee.as_view(), name="create_employee"),
    path("edit/<int:id>/", EditEmployee.as_view(), name="edit_employee"),
    path("delete/<int:id>/", DeleteEmployee.as_view(), name="delete_employee"),
]
