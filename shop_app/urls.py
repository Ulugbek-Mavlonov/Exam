from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login_user, name='login' ),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('add_basket', views.add_basket, name='add_basket'),
    path('basket/', views.basket, name='basket'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('order/<int:user_id>/', views.order, name='order'),
    path('history/<int:user_id>/', views.history, name='history')
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

