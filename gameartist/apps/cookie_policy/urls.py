from django.urls import path

from . import views

urlpatterns = [
    path(r'policy/', views.policy_view, name='cookiePolicy'),
    path(r'accept-cookie-policy/', views.accept_cookie_policy_view, name='acceptCookiePolicy'),
]
