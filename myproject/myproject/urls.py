from django.urls import path
from nmcnpmapp import views
from nmcnpmapp.views import SignUpView
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
