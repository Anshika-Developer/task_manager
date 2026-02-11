from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from .models import Task

def task_list(request):
    status = request.GET.get('status')
    priority = request.GET.get('priority')

    tasks = Task.objects.all()

    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)

    tasks = tasks.order_by('-created_at')

    stats = Task.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        pending=Count('id', filter=Q(status='PENDING')),
    )

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'stats': stats,
        'status': status,
        'priority': priority,
    })


def task_create(request):
    if request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST.get('description', ''),
            priority=request.POST.get('priority', 'MEDIUM')
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        task.status = request.POST['status']
        task.priority = request.POST['priority']
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
