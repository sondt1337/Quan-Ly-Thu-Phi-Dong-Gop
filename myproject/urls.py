from django.urls import path
from nmcnpmapp import views
from nmcnpmapp.views import SignUpView, about, contact
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("wait/", views.wait, name="wait"),
    # path('view_family_members/', views.view_family_members, name='view_family_members'),
    # path('view_family_members/<str:group_name>/', views.view_family_members, name='view_family_members_with_group'),
    # path('view_family_members/', views.view_family_members, name='view_family_members'),
]