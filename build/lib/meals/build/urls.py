from django.conf.urls import url

from meals.build.view_environments.login_.router import login_
from meals.build.view_environments.logout_.router import logout_


urlpatterns = [
    url(r'^login/$', login_),
    url(r'^logout/$', logout_),
]
