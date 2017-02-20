from django.conf.urls import url
from simplemooc.core import views as courseViews

urlpatterns = [
	    url(r'^$', courseViews.home ,name='index'),

]
