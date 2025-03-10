from django.conf import settings  
from django.contrib import admin
from django.urls import path, include

urlpatterns = [  
    path("admin/", admin.site.urls),
    path("", include("todos.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path("debug/", include(debug_toolbar.urls)),
    ]