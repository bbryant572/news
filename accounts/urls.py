from django.urls import path


from .views import SignUpView
from .views import PasswordChangeView, PasswordChangeSuccessView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/<int:pk>',
         PasswordChangeView.as_view(), name='password_change'),
    path('password_change/success/',
         PasswordChangeSuccessView.as_view(), name='password_success'),
]
