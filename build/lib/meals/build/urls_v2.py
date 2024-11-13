from django.conf.urls import url, include

from meals.build.view_environments.login_.router import login_
from meals.build.view_environments.logout_.router import logout_


base_path = "api/meals/"

api_paths = [
    url(r'^login/$', login_),
    url(r'^logout/$', logout_),
]


urlpatterns = [
    url(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
