from django.shortcuts import render, get_object_or_404, redirect
from .models import Play, Actor
from .forms import PlayForm, ActorForm

def play_detail(request, play_id):
    play = get_object_or_404(Play, pk=play_id)
    return render(request, 'theater/play_detail.html', {'play': play})

def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    return render(request, 'theater/actor_detail.html', {'actor': actor})

def play_create(request):
    if request.method == 'POST':
        form = PlayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PlayForm()
    return render(request, 'theater/play_form.html', {'form': form})

def play_edit(request, play_id):
    play = get_object_or_404(Play, pk=play_id)
    if request.method == 'POST':
        form = PlayForm(request.POST, request.FILES, instance=play)
        if form.is_valid():
            form.save()
            return redirect('play_detail', play_id=play.id)
    else:
        form = PlayForm(instance=play)
    return render(request, 'theater/play_form.html', {'form': form})

def actor_create(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ActorForm()
    return render(request, 'theater/actor_form.html', {'form': form})

def actor_edit(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor_detail', actor_id=actor.id)
    else:
        form = ActorForm(instance=actor)
    return render(request, 'theater/actor_form.html', {'form': form})
