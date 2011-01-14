from zope.configuration import xmlconfig
from webob import Request
from pyramid.interfaces import IRequest
from pyramid.testing import DummyModel
from zope.interface import alsoProvides

DummyContext = DummyModel
def DummyRequest(*args, **kwargs):
    request = Request.blank(*args, **kwargs)
    alsoProvides(request, IRequest)
    return request

def configure(configuration_string):
    xmlconfig.string(configuration_string, execute=True)