from django.contrib import admin
from django.urls import path, include

from accounts.views import home_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),

]

