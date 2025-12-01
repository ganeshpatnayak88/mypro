from django.urls import path
from .views import home, register_page, login_page, dashboard_page
from .api import register_api, login_api

urlpatterns = [
    path("", home),
    path("register/", register_page),
    path("login/", login_page),
    path("dashboard/", dashboard_page),

    # APIs
    path("api/register/", register_api),
    path("api/login/", login_api),
]
