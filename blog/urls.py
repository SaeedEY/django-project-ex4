from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts,name='posts'),
    path('article/<int:post_id>',views.post,name='post'),
    path('tag/<str:tag_name>',views.tag,name='tag'),
    path('404',views.pnf404,name='pnf404')
]