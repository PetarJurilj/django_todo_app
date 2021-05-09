from django.urls import path
from .views import TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView, TaskCreateView, CustomLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('edit-task/<int:pk>/', TaskUpdateView.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
    path('create-task/', TaskCreateView.as_view(), name='create-task'),

    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout")
]
