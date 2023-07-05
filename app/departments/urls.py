from django.urls import path

# from .views import CreateDepartment
# from .views import DeleteDepartment
# from .views import EditDepartment
from .views import ListDepartments


urlpatterns = [
    path("", ListDepartments.as_view(), name="departments_list"),
]
