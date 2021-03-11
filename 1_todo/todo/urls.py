from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:itemId>', views.todo_item, name = 'detail'),
    path('add_item', views.add_item, name = 'add item'),
    path('complete/<int:listId>', views.complete, name = 'change status'),
    path('delete/<int:listId>', views.delete, name = 'change status')
]