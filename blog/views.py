from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm
# Create your views here.


def blog_post_list_view(request):
    # list out objects
    # could be search view
    template_name = 'blog/list.html'
    # qs = BlogPost.objects.all().published()
    qs = BlogPost.objects.published()
    context = {
        'object_list': qs
    }
    return render(request, template_name, context)


@login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    template_name = 'blog/form.html'
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.title = form.cleaned_data.get('title') + "xyz"
            obj.user = request.user
            obj.save()
            form.save()  # can do this as this form is modal form
            form = BlogPostModelForm()
    else:
        form = BlogPostModelForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


# def blog_post_create_view(request):
#     # create objects
#     # ? use a form
#     template_name = 'blog/form.html'
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST or None)
#         if form.is_valid():
#             # form.save() can't do this as this form is not modal form
#             BlogPost.objects.create(**form.cleaned_data)
#             form = BlogPostForm()
#     else:
#         form = BlogPostForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    template_name = 'blog/detail.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    template_name = 'blog/update.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
    else:
        form = BlogPostModelForm(instance=obj)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    template_name = 'blog/delete.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        obj.delete()
        return redirect('/blog')
    context = {
        'object': obj
    }
    return render(request, template_name, context)
