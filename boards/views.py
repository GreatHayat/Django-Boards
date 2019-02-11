from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board
# Create your views here.
def index(request):
    context = {
        "boards": Board.objects.all()
    }
    return render(request, 'boards/index.html', context)

def board_topics(request, id):
    board = get_object_or_404(Board, id = id)
    return render(request, 'boards/topics.html', {"board": board})