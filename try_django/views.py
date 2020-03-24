from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
from blog.models import BlogPost
from .forms import ContactForm


def home_view(request):
    qs = BlogPost.objects.all()[:5]
    context = {
        "title": "Welcome to Try Django",
        'blog_list': qs
    }
    return render(request, 'home.html', context)


def about_view(request):
    return render(request, 'hello_world.html', {"title": "About Us"})


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {
        "title": "Contact Us",
        'form': form
    }
    return render(request, 'form.html', context)


# def example_page(request):
#     # With HttpResponse Method
#     # context = {"title": "Example"}
#     # template_name = 'hello_world.html'
#     # template_obj = get_template(template_name)
#     # rendered_item = template_obj.render(context)
#     # return HttpResponse(rendered_item)
#     # With Render Method
#     context = {"title": "Example 2"}
#     template_name = 'title.txt'
#     template_obj = get_template(template_name)
#     rendered_item = template_obj.render(context)
#     print(rendered_item)
#     return render(request, 'hello_world.html', {"title": rendered_item})
