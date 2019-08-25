from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'<int:year>/<int:month>/<int:day>/<slug:slug>', views.Single.as_view(), name='single'),
]
