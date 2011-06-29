from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^user/', include('django.contrib.auth.urls')), 

	# Example:
	(r'^list(\?.*)?$', 'cmmntr.views.convlist'),
	(r'^conversation/(.*)$', 'cmmntr.views.conversation'),
	(r'^post/(.*)$', 'cmmntr.views.postcomment'),
	(r'^$', 'cmmntr.views.index'),
)
