from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("create/", views.Create_account.as_view(), name="create_account"),
    path("data_view/", views.data_view, name="data_view"),
]