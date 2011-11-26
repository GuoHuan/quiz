from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from question.views import show_question_by_id,show_all_questions,quiz
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiz.views.home', name='home'),
    # url(r'^quiz/', include('quiz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'$^',direct_to_template,{'template':'index.html'}),
	url(r'^q/(?P<q_id>\d+)/$',show_question_by_id),
	url(r'^qall/$',show_all_questions),
	url(r'^create_quiz/$',direct_to_template,{'template':'c_quiz.html'}),
	url(r'^quiz/$',quiz),
)
