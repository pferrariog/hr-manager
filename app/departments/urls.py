from django.urls import path

from .views import CreateDepartment
from .views import DeleteDepartment
from .views import EditDepartment
from .views import ListDepartments


urlpatterns = [
    path("", ListDepartments.as_view(), name="departments_list"),
    path("new/", CreateDepartment.as_view(), name="create_department"),
    path("edit/<int:id>", EditDepartment.as_view(), name="edit_department"),
    path("delete/<int:id>", DeleteDepartment.as_view(), name="delete_department"),
]
