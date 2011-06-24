from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^user/', include('django.contrib.auth.urls')), 

	# Example:
	(r'^list(\?.*)?$', 'server.cmmntr.views.convlist'),
	(r'^conversation/(.*)$', 'server.cmmntr.views.conversation'),
	(r'^post/(.*)$', 'server.cmmntr.views.postcomment'),
)
