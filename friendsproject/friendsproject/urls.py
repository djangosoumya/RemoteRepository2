"""friendsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from friendsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_friends),
    # path('data/',views.display_friends,name='data')
    path('update_friends/<id>',views.update_friends,name='update_friends'),
    path('update_friends_save/<id>',views.update_friends_save,name='update_friends_save'),
    path('delete_friends/<id>',views.delete_friends,name='delete_friends')
]
