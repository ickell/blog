"""blogmodel URL Configuration

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
from django.contrib import admin
from django.urls import path
import main.views
import portf.views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="home"),
    path('search/', main.views.search, name="search"),
    path('write/', main.views.write, name = "write"),
    path('create/', main.views.create, name = "create"),
    path('n/<int:post_id>', main.views.detail, name ="detail"),
    path('portf/', portf.views.pf, name ="pf"),
    path('writeimage/', portf.views.CreatePostView.as_view(), name ="writeimage"),
    path('delete/<int:post_id>', main.views.delete, name ="delete"),
    path('update/<int:post_id>', main.views.update, name ="update"),
    path('comment_write/<int:post_pk>/', main.views.comment_write, name="comment_write"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
