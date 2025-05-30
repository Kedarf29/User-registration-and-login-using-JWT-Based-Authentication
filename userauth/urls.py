from django.urls import path, include
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from .views import (
    api_home,
    CustomRegistrationView,
    CustomLoginView,
    AuthenticatedUserAPIView,
    PasswordChangeView
)


urlpatterns = [
    # path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    # path("password/reset/", PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password/reset/confirm/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),

    path('home', api_home, name='api-home'),
    path("registration/", CustomRegistrationView.as_view(), name="custom-registration"),
    path("login/", CustomLoginView.as_view(), name="custom-login"),
    path("user/", AuthenticatedUserAPIView.as_view(), name="auth-user"),
     path("password/change/", PasswordChangeView.as_view(), name="password_change"),


    
]
