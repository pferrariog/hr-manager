from django.urls import path

from .views import CompanyCreate
from .views import CompanyEdit


urlpatterns = [
    path("new", CompanyCreate.as_view(), name="create_company"),
    path("edit/<int:id>", CompanyEdit.as_view(), name="edit_company"),
]
