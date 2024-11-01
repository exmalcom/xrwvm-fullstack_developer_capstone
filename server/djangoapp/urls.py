from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import registration, login_user, logout_request
from . import views


app_name = 'djangoapp'
urlpatterns = [
    path(route='register', view=registration, name='register'),
    path(route='login', view=login_user, name='login'),
    path(route='logout', view=logout_request, name='logout'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
