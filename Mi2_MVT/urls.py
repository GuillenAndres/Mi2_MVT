from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Mi_Familia/', include('Mi_Familia.urls'))
]
