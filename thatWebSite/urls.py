"""thatWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
import actions
import show

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',actions.sayHello),
    url('^signup$',actions.getSignup),
    url('upload',actions.getUpload),

    url('^([a-z1-9]+)/([a-z1-9A-Z]+.[a-z1-9A-Z]+)',actions.sayHtml), #仅支持 xxx.com:80/xxx/xxx.xxx 格式(即一重文件夹+文件名.xxx)




    url('',actions.say404)

]
