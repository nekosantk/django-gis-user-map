from django.urls import path
from .views import HomepageView, RegisterView, profile


"""
Specifies inner urls routes
"""

urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path('register/', RegisterView.as_view(), name='user-register'),
    path('profile/', profile, name='user-profile'),
]
