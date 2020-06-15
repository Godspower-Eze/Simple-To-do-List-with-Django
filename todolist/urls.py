from django.urls import path, include
from .views import index, update

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:task_id>', update, name='update')
]
