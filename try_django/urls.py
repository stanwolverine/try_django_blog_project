"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include  # re_path and url
from blog.views import blog_post_create_view
from .views import (
    home_view,
    about_view,
    contact_view,
    # example_page
)

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('blog-new/', blog_post_create_view, name='blog-create'),
    path('blog/', include('blog.urls')),
    # path('example/', example_page, name='example'),
    path('admin/', admin.site.urls),
    # '''
    # > Same view for two or more different paths?
    # > we can use one view for two or more url strings using "re_path"
    # > i.e.
    # > re_path(r'^pages?/$', about_page)
    # > Above will render for both 'page' and 'pages' url string
    # '''
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
