from django.urls import path
from .views import index, sign_in, register, logout_user, blog, qa, ops, cab, cabinet, presentation


urlpatterns = [
    path('', index, name='homepage'),
    path('blog', blog, name='blog'),
    path('qa', qa, name='qa'),
    path('login', sign_in, name='login-page'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('ops', ops, name='ops'),
    path('cab', cab, name='cab'),
    path('cabinet', cabinet, name='cabinet'),
    path('presentation', presentation, name='presentation'),

]
