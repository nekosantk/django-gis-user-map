from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usermap.views import CustomLoginView
from usermap.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usermap.urls')),
    path('login/', CustomLoginView.as_view(
        redirect_authenticated_user=True,
        template_name='login.html',
        authentication_form=LoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout.html'),
         name='logout'),
]
