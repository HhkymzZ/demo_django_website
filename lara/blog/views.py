from .models import Post
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"index.html")

def postlar(request):
    pics = Post.objects.all()
    return render(request,"postlar.html",{"pics":pics})

