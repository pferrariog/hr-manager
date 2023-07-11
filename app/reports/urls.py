from django.urls import path

from .views import CreateDocument


# from .views import DeleteDocument


urlpatterns = [
    path("new/<int:id>", CreateDocument.as_view(), name="create_document"),
    # path("delete/<int:id>", DeleteDocument.as_view(), name="delete_document"),
]
