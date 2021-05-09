from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView, CreateView

from django.contrib.auth.views import LoginView

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'task/login.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task/tasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = context['tasks']
        tasks = tasks.filter(user=self.request.user)
        context['count'] = tasks.filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            tasks = tasks.filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context



class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "task/task_detail.html"


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = "task/task_update.html"
    success_url = reverse_lazy('tasks')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/task_delete.html"
    success_url = reverse_lazy('tasks')


class TaskCreateView(CreateView):
    model = Task
    template_name = "task/task_create.html"
    fields = '__all__'
    success_url = reverse_lazy('tasks')
