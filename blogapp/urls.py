from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.Create, name='create')
]
