from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.homePageView, name = "home"),
    path("nextPage/", views.newPage, name = "next"),
    path("anotherPage/", views.AnotherPage.as_view(), name = "another"),
    path("redirectionPage/", views.RedirectPage.as_view(), name = "redirect")
]
