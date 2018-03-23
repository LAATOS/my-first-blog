from django.shortcuts import render

# Create your views here.
def post_list(request):
    """

    :type request: object
    """
    return render(request, 'blog/post_list.html', {})