from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .auth import check_blog_author


def index(request):
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


@login_required
def new_blog(request):

    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        if check_blog_author(request, blog_id):
            form = BlogForm(instance=blog)
        else:
            raise Http404
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog', args=[blog_id]))

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)




