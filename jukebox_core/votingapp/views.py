from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Songs
from django.shortcuts import render, get_object_or_404


def index(request):
    songs = Songs.objects.all()
    return render(request, 'votingapp/polls.html', {'songs': songs})


def vote(request):
    songs = Songs.objects.all()
    try:
        selected_song = get_object_or_404(Songs, pk = request.POST["choice"])
    except:
        return render(request, "votingapp/polls.html", {'songs': songs, 'error_msg': "Please select a choice to vote"})
    else:
        selected_song.votes += 1
        selected_song.save()
        sorted_songs = Songs.objects.order_by('-votes').all()
        return HttpResponseRedirect(reverse('play'), {'songs': sorted_songs})


def play(request):
    sorted_songs = Songs.objects.order_by('-votes').all()
    print(sorted_songs)

    return render(request, "votingapp/play.html", {'songs': sorted_songs})
