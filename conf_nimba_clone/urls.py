from django.contrib import admin
from django.urls import path, include

import sms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sms.urls'))
]
