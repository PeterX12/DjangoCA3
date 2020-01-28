from django.shortcuts import render
from .models import Board, Topic
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards':boards})

def board_topics(request, pk):
    #board = get_object_or_404(Boards, pk=pk)
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
