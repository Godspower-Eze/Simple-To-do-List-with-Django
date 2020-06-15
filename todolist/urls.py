from django.urls import path, include
from .views import index, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:task_id>', update, name='update'),
    path('delete/<int:task_id>', delete, name='delete')
]
