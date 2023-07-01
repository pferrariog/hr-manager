from django.urls import path

from .views import CreateCompany
from .views import EditCompany


urlpatterns = [
    path("new", CreateCompany.as_view(), name="create_company"),
    path("edit/<int:id>", EditCompany.as_view(), name="edit_company"),
]
