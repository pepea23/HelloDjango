from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tddtests.urls')),
    # path('words/', include('tddtests.urls')),
    path('polls/', include('polls.urls')),
    path('stock/', include('stock.urls')),
]
