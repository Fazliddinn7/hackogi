from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', RegisterView.as_view(), name='signup_page'),
]
