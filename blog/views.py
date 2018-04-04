from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    """

    :type request: object
    """
    return render(request, 'blog/post_list.html', {})

def post_list(request):
    post = Post.objects.filtrt(published_date_lte=timezone.now().order_by('published_date'))
    return render(request, 'blog/post_list.html', {'posts': posts})
