from os import name
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import UpdateAgreementView




urlpatterns = [
   
    path('', views.index,name='index'),
    path('account/', include('django.contrib.auth.urls')),
    path('home', views.home,name='home'),
    path('agreements', views.agreements, name='agreements'),
    path('agreement/<id>', views.view_agreement, name='single_agreement'),
    path('update-agreement/<int:pk>', UpdateAgreementView.as_view(), name='update-agreement'), 
    # path('<pk>/delete', AgreementDeleteView.as_view()),
    path('delete-agreement/<id>', views.delete_agreement, name='delete_agreement'),
    path('inventory', views.inventory, name='inventory'),
    path('inventory/<id>', views.view_inventory, name='single_inventory'),
    path('update-inventory/<id>', views.update_inventory, name='update_inventory'),
    path('download/', views.download_file, name='download_file'),
    path('focal', views.focal_points, name='focal'),
   



    # path('search/', views.search, name='search_business'),
   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)






