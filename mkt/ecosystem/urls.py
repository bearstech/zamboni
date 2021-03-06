from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url('^$', views.landing, name='ecosystem.landing'),
    url('^partners$', views.partners, name='ecosystem.partners'),
    url('^support$', views.support, name='ecosystem.support'),
    url('^dev_phone$', views.dev_phone, name='ecosystem.dev_phone'),
    url('^docs/app_generator$', views.app_generator_documentation,
        name='ecosystem.app_generator_documentation'),
    url('^docs/firefox_os_simulator$', views.firefox_os_simulator,
        name='ecosystem.firefox_os_simulator'),
    url('^docs/(?P<page>\w+)?$', views.documentation,
        name='ecosystem.documentation'),
    url('^docs/apps/(?P<page>\w+)?$', views.apps_documentation,
        name='ecosystem.apps_documentation'),
)
