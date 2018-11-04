from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name = 'grievance'

urlpatterns = [

    # url('^admin/', admin.site.urls),
    url(r'^posts/$',views.PostListView.as_view(),name='post_list'),
    url(r'^addcomment/(?P<post_id>\d+)/$',views.add_comment_view,name='add_comment'),
    url(r'^adminreply/(?P<pk>\d+)/$',views.admin_reply_comment, name='reply_admin'),
    url(r'^add_upvotes/(?P<post_id>\d+)/$',views.add_upvotes, name='add_upvotes'),
    url(r'^addgrievance/$',views.PostCreateView.as_view(), name='add_post'),



]
