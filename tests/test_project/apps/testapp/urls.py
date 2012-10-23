from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, HttpBasicSimple

from test_project.apps.testapp.handlers import EntryHandler, ExpressiveHandler, AbstractHandler, EchoHandler, PlainOldObjectHandler, Issue58Handler, Issue192Handler, ListFieldsHandler

auth = HttpBasicAuthentication(realm='TestApplication')

entries = Resource(handler=EntryHandler, authentication=auth)
expressive = Resource(handler=ExpressiveHandler, authentication=auth)
abstract = Resource(handler=AbstractHandler, authentication=auth)
echo = Resource(handler=EchoHandler)
popo = Resource(handler=PlainOldObjectHandler)
list_fields = Resource(handler=ListFieldsHandler)
issue58 = Resource(handler=Issue58Handler)
issue192 = Resource(handler=Issue192Handler)
fileupload = Resource(handler=FileUploadHandler)
circular_a = Resource(handler=CircularAHandler)

AUTHENTICATORS = [auth,]
SIMPLE_USERS = (('admin', 'secr3t'),
                ('admin', 'user'),
                ('admin', 'allwork'),
                ('admin', 'thisisneat'))

for username, password in SIMPLE_USERS:
    AUTHENTICATORS.append(HttpBasicSimple(realm='Test', 
                            username=username, password=password))

multiauth = Resource(handler=PlainOldObjectHandler, 
                        authentication=AUTHENTICATORS)

urlpatterns = patterns(
    '',
    url(r'^entries/$', entries),
    url(r'^entries/(?P<pk>.+)/$', entries),
    url(r'^entries\.(?P<emitter_format>.+)', entries),
    url(r'^entry-(?P<pk>.+)\.(?P<emitter_format>.+)', entries),

    url(r'^issue58\.(?P<emitter_format>.+)$', issue58),
    url(r'^issue192\.(?P<emitter_format>.+)$', issue192),

    url(r'^expressive\.(?P<emitter_format>.+)$', expressive),

    url(r'^abstract\.(?P<emitter_format>.+)$', abstract),
    url(r'^abstract/(?P<id_>\d+)\.(?P<emitter_format>.+)$', abstract),

    url(r'^echo$', echo),
    
    url(r'^file_upload/$', fileupload, name='file-upload-test'),

    url(r'^multiauth/$', multiauth),

    url(r'^circular_a/$', circular_a),

    # oauth entrypoints
    url(r'^oauth/request_token$', 'piston.authentication.oauth_request_token'),
    url(r'^oauth/authorize$', 'piston.authentication.oauth_user_auth'),
    url(r'^oauth/access_token$', 'piston.authentication.oauth_access_token'),

    url(r'^list_fields$', list_fields),
    url(r'^list_fields/(?P<id>.+)$', list_fields),
    
    url(r'^popo$', popo),
)


