from django.urls import path
from .views import cabinet, homework


urlpatterns = [
    path('cabinet', cabinet, name='cabinet'),
    path('homework', homework, name='homework'),

]
