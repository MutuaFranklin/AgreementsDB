from os import name
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   
    path('', views.index,name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('home', views.home,name='home'),
    path('agreements', views.agreements, name='agreements'),
    path('agreement/<id>', views.view_agreement, name='single_agreement'),
    path('update-agreement/<id>', views.update_agreement, name='update_agreement'),
    path('inventory', views.inventory, name='inventory'),
    path('inventory/<id>', views.view_inventory, name='single_inventory'),
    path('update-inventory/<id>', views.update_inventory, name='update_inventory'),
    path('download/', views.download_file, name='download_file'),
    path('focal', views.focal_points, name='focal'),


    # path('search/', views.search, name='search_business'),
   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






