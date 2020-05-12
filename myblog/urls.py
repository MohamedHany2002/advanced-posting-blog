
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name='posts'),
    path('tag/<slug:tag_slug>', views.post_list,name='tagged_posts'),
    # path('', views.list_posts.as_view(),name='allposts'),
    path('<slug:slug>', views.post_detail,name='detail'),
    path('emailview/<int:id>', views.sending_email,name='send_email'),
    # path('comment/<int:id>', views.comment_post,name='comment'),

]
