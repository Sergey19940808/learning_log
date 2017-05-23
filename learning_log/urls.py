"""learning_log URL Configuration

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
# imports
from django.conf.urls import include, url
from django.contrib import admin


# url's for others app
urlpatterns = [

    # add apps
    url(r'^', include('learning_logs.urls', namespace='learning_logs')),
    url(r'^users/', include('users.urls', namespace='users')),
    # url(r'^training/', include('training.urls', namespace='training')),
    url(r'^nice_chips/', include('nice_chips.urls', namespace='nice_chips')),

    # integreted urlconf
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    # standart urlconf
    url(r'^admin/', admin.site.urls)
]