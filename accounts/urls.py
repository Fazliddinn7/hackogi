from django.urls import path

from accounts.views import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
]
