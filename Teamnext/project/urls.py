from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def google_verify(request):
    return HttpResponse("google-site-verification: google05aabfcd698e02fd.html", content_type="text/html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("google05aabfcd698e02fd.html", google_verify),
    path('', include('myapp.urls')),
]