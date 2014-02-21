from django.conf.urls import patterns, url

urlpatterns = patterns('myblog.views',
    url(r'^$',
        'list_view',
        name="list_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        'detail_view',
        name="blog_detail")


)