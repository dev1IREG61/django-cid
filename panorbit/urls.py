from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static   # 👈 needed for static()

def home(request):
    return HttpResponse("helo bro")

urlpatterns = [
    path('', home, name='home'),              # Root URL
    path('admin/', admin.site.urls),
    path('world/', include('world.urls')),    # Your app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
