from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contect, name='contact'),
    path('services/<servd>', views.services, name='service-details'),  
    path('term-conditions', views.termconditions, name='term-conditions'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
