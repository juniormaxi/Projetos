from django.conf.urls import url
from simplemooc.core import views as coreViews

urlpatterns = [
	    url(r'^$', coreViews.home ,name='home'),
	    url(r'^contato/', coreViews.contact, name='contact'),
]
