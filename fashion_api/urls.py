from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fashion.urls')),  # ✅ Make sure this is not commented out
]
