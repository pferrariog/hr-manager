from core.views import UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from employees.views import EmployeeViewSet
from overtime.views import OvertimeViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"employee", EmployeeViewSet)
router.register(r"overtime", OvertimeViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("api/", include(router.urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    path("company/", include("companies.urls")),
    path("department/", include("departments.urls")),
    path("employee/", include("employees.urls")),
    path("overtime/", include("overtime.urls")),
    path("report/", include("reports.urls")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
