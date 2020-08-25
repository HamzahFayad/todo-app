from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'all_tasks'
    template_name = 'task-list.html'


def task_list(request):
    logged_in_user = request.user
    # all_the_tasks = Task.objects.all()
    all_the_tasks = Task.objects.filter(user=logged_in_user)

    context = {'all_tasks': all_the_tasks}
    return render(request, 'task-list.html', context)


class TaskDetailsView(DetailView):
    model = Task
    context_object_name = 'one_task'
    template_name = 'task-details.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task-create.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if not form.is_valid():
            return False
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'delete_one'
    template_name = 'task-delete.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('text', 'task_photo')
    template_name = 'edit-task.html'
    pk_url_kwarg = 'pkc'
    context_object_name = 'task'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return redirect('task-list')


def task_delete(request, **kwargs):
    task_id = kwargs['pkc']
    context = {}
    if request.method == 'POST':
        Task.objects.filter(id=task_id).delete()
        return redirect('task-list')
    return render(request, 'task-delete.html', context)