from django.urls import path

# from .views import CreateOvertimeRegister
# from .views import DeleteOvertimeRegister
from .views import EditOvertimeRegister
from .views import ListOvertimeRegisters


urlpatterns = [
    path("", ListOvertimeRegisters.as_view(), name="overtime_list"),
    # path("new/", CreateOvertimeRegister.as_view(), name="create_overtime_register"),
    path("edit/<int:id>", EditOvertimeRegister.as_view(), name="edit_overtime_register"),
    # path("delete/<int:id>", DeleteOvertimeRegister.as_view(), name="delete_overtime_register"),
]
