from django.shortcuts import render
from .models import SearchQuery
from blog.models import BlogPost
# Create your views here.


def search_view(request):
    user = None
    query = request.GET.get('q', None)
    blog_list = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
    context = {
        'query': query,
        'blog_list': blog_list
    }
    return render(request, 'searches/view.html', context)
