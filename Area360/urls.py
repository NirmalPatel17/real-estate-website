from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('property/',views.property, name="property"),
    path('property-single',views.propertysingle, name="propertysingle"),

    path('auth/register/',views.user_register, name="register"),
    path('auth/login/',views.user_login, name="login"),
    # path('token/',views.token, name = 'token'),
    path('verify/<auth_token>',views.verify, name = 'verify'),
    path('auth/logout/',views.user_logout, name = 'logout'),
]
