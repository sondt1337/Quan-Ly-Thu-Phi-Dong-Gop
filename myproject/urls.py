from django.urls import path
from nmcnpmapp import views
from nmcnpmapp.views import SignUpView, about, contact
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordChangeView
from nmcnpmapp.views import password_change_done
from django.conf import settings
from django.conf.urls.static import static

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
    path("notification/", views.notification, name="notification"),
    path("personal/", views.personal, name="personal"),
    path("changepassword/", views.changepassword, name="changepassword"),
    path('change-password/', PasswordChangeView.as_view(success_url='/change-password-done/'), name='password_change'),
    path('change-password-done/', password_change_done, name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)