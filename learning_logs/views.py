# imports
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# views index
def index(request):
    title = 'Домашняя'
    context = {'title': title}
    return render(request, 'learning_logs/index.html', context)

# views topics
@login_required
def topics(request):
    title = 'Список ваших тем'
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics, 'title': title}
    return render(request, 'learning_logs/topics.html', context)

# views topic
@login_required
def topic(request, topic_id):
    title = 'Список записей в теме'
    topic = get_object_or_404(Topic, id=topic_id)

    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries, 'title': title}
    return render(request, 'learning_logs/topic.html', context)




# views add topic
@login_required
def new_topic(request):
    title = 'Добавление новой темы'
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
        return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form, 'title': title}
    return render(request, 'learning_logs/new_topic.html', context)


# views add entries
@login_required
def new_entry(request, topic_id):
    title = 'Добавление новой записи в тему'
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form, 'title': title}
    return render(request, 'learning_logs/new_entry.html', context)


# views edit entry
@login_required
def edit_entry(request, entry_id):
    title = 'Редактирование выбранной записи'
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form, 'title': title}
    return render(request, 'learning_logs/edit_entry.html', context)


# views delete entry
@login_required()
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404

    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))


# views edit topic
@login_required()
def edit_topic(request, topic_id):
    title = 'Редактирование выбранной темы'
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TopicForm(instance=topic)

    else:
        form = TopicForm(instance=topic, data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'topic': topic, 'form': form, 'title': title}
    return render(request, 'learning_logs/edit_topic.html', context)


# views for delete topic
@login_required()
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if topic.owner != request.user:
        raise Http404

    topic.delete()
    return HttpResponseRedirect(reverse('learning_logs:topics'))


