
from django.contrib import admin
from django.urls import path, include

# ficam todas as urls
urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
]
