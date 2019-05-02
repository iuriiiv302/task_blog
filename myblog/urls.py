"""myblog URL Configuration

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
from django.urls import include
from blogg.views import get_list, get_post, get_voting
from rest_framework import routers
from apiauth import views
from rest_framework_swagger.views import get_swagger_view
from blogexemple.views import index, view_post, view_category

schema_view = get_swagger_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'votes',views.VotingViewSet)


urlpatterns= [
    path('admin/', admin.site.urls),
    path('list/', get_list, name='get_list'),
    path('blog/', get_post, name='get_post'),
    path('blog/vote/<int:post_id>', get_voting, name="voting_post"),

    path('exemple/', index, name='blogview'),
    path('blog/view/',view_post, name ='view_blog_post'),
    path('blog/category/',view_category, name = 'view_category'),


    path('swager/',schema_view),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace ='rest_framework')),
]
