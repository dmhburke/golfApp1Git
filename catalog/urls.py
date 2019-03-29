from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='playgolf'),
    path('latourette/', views.latourette.as_view(), name='latourette'),
    path('latourette/scoreboard', views.latourette_scoreboard, name='scoreboard'),
    path('latourette/<int:pk>', views.holedetail_view, name='holedetail'),
]
