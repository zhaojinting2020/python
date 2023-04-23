from django.shortcuts import render

from .models import Topic
from .forms import TopicForm

from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        # print(request.method)
        # print("empty new topic")
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        
        if form.is_valid():
            print("valid new topic")
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    # request is get or the post request is invalid
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)