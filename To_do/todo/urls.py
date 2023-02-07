from django.urls import path

from .views import index, set_task_as_completed, del_task, set_task_as_no_completed, set_all_completed

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/completed', set_task_as_completed, name='set_completed'),
    path('<int:id>/no_completed', set_task_as_no_completed, name='no_completed'),
    path('<int:id>/delete', del_task, name="delete_task"),
    path('set_all_completed/', set_all_completed, name='set_all_completed'),

]


