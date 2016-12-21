"""goiztiri URL Configuration

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
from personas.views import HomeView, PersonaCreationView, PersonaDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alta$', PersonaCreationView.as_view(), name='alta_persona'),
    url(r'^photos/(?P<pk>[0-9]+)$', PersonaDetailView.as_view(), name='photos_detail'),
    url(r'^$', HomeView.as_view(), name='goiztiri_home'),
]
