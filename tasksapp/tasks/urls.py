from django.urls import path

from .views import index, TaskListView, TaskDetailView, task_list, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('list', task_list, name='list'),
    path('<int:pk>/detail', TaskUpdateView.as_view(), name='task-detail'),
    path('create', TaskCreateView.as_view(), name='create'),
]
app_name = 'tasks'
