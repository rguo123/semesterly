from django.conf.urls import patterns, include, url

from django.contrib import admin

# from haystack.views import SearchView

# from haystack.query import SearchQuerySet

admin.autodiscover()

# custom 404 page
handler404 = 'timetable.views.custom_404'

	# for sorting search results by course code
	# sqs = SearchQuerySet().order_by('code')

urlpatterns = patterns('',
	# url(r'^admin/', include(admin.site.urls)),

	# index
	url(r'^timetable/*$', 'timetable.views.redirect_to_home'),
	url(r'^timetable/.+$', 'timetable.views.redirect_to_home'),
	url(r'^tt_course_search/*$', 'timetable.views.tt_course_search'),

	url(r'^AX82mA2jjQ3r1z/*$', 'analytics.views.handle_user_info_request'),
	url(r'^exit/*$', 'analytics.views.handle_exit'),

	url(r'^analytics/*$', 'analytics.views.view_analytics_dashboard'),
	url(r'^analytics_data/*$', 'analytics.views.get_analytics_data'),
	url(r'^timetable_data/*$', 'analytics.views.get_timetable_data'),

	url(r'^live_user_data/*$', 'analytics.views.get_live_user_data'),
	url(r'^reason/*$', 'analytics.views.verify_password'),
	url(r'^courses/(?P<school>.+?)/(?P<sem>[fFsS]{1}?)/*$', 'timetable.views.get_courses'),
	url(r'^courses/(?P<school>.+?)/id/(?P<id>[0-9]+)/*$', 'timetable.views.get_course'),
	url(r'^populate/*$', 'timetable.views.do_all'),
	url(r'^/*.*$', 'timetable.views.view_timetable'),

)