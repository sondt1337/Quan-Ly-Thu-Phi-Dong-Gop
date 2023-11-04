
from django.urls import path
from myapp import views
from myapp.views import SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
]