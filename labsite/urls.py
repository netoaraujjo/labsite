"""labsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from members import views as members_views
from researches import views as researches_views

urlpatterns = [
    url(r'^members/$', members_views.index, name='members_index'),
    url(r'^research_lines/$', researches_views.research_lines, name='research_lines_index'),
    url(r'^publications/$', researches_views.publications, name='publications_index'),
    url(r'^admin/', admin.site.urls),
]
