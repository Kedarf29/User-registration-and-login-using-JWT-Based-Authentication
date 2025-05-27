from django.urls import path, include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from .views import api_home


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
     path('home', api_home, name='api-home'),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("password/reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
