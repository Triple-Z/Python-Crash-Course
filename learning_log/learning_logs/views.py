from django.shortcuts import render

def index(request):
    """ Main page of learning logs """
    return render(request, 'learning_logs/index.html')
