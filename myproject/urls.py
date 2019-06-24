"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views as my_views

admin.autodiscover()

urlpatterns = [
    url(r'^$', my_views.hello, name='hello'),
    url(r'^hello/(\w+)/$', my_views.hello_name, name='hello name'),
    url(r'^books/$', my_views.all_books, name='books'),
    url(r'^books/(\d+)/', my_views.get_book, name='my book'),
    url(r'^admin/', admin.site.urls),
]
