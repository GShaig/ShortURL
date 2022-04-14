from django.urls import path, include

from .views import index_view, redirect_view

from allauth.account.views import LoginView

appname = "shorturl"

urlpatterns = [
    path("", LoginView.as_view(), name="account_login"),
    path('<str:shortened_part>', redirect_view, name='redirect'),
    path('accounts/', include('allauth.urls')),
    path('service/', index_view, name='index'),
]
