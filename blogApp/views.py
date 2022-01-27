from django.shortcuts import render
from blogApp.models import *
# Create your views here.
def blog(request):
    
    blogs=post.objects.all()
    return render(request, "blog/blog.html",{'blogs':blogs})#esto ultimo es para pasar los datos al html