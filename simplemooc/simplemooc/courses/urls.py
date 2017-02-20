from django.conf.urls import url
from simplemooc.courses import views as courseViews

urlpatterns = [
	    url(r'^$', courseViews.index, name='index'),
	    url(r'^(?P<pk>\d+)/$', courseViews.details, name='details'),
]
