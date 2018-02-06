from .models import BlogPost


def check_blog_author(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)

    if request.user == blog.author:
        return True
    else:
        return False

