import re

from zope import interface
from zope import component

from chameleon.core import types
from chameleon.zpt.expressions import ExpressionTranslator
from chameleon.zpt.interfaces import IExpressionTranslator

from pyramid_skins.interfaces import ISkinObject
from pyramid.url import route_url

class SkinTranslator(ExpressionTranslator):
    interface.implements(IExpressionTranslator)

    symbol = '_lookup_skin'
    re_path = re.compile(r'^[A-Za-z./_\-]+$')

    def translate(self, string, escape=None):
        if not string:
            return None
        string = string.strip()

        if self.re_path.match(string) is None:
            raise SyntaxError(string)

        value = types.value("%s('%s', template)" % (self.symbol, string))
        value.symbol_mapping[self.symbol] = _lookup_skin
        return value

class RouteTranslator(ExpressionTranslator):
    interface.implements(IExpressionTranslator)

    symbol = '_route_url'

    def translate(self, string, escape=None):
        if not string:
            return None
        string = string.strip()
        value = types.value("%s('%s', request, subpath='').rstrip('/')" % (
            self.symbol, string))
        value.symbol_mapping[self.symbol] = route_url
        return value

def _lookup_skin(name, template):
    if name.startswith('/'):
        return component.getUtility(ISkinObject, name=name[1:])
    if not ISkinObject.providedBy(template):
        raise TypeError(
            "Relative lookup for '%s' invalid for template class: %s." % (
                name, type(template)))
    path = '/' + template.name
    while path:
        inst = component.queryUtility(ISkinObject, name="%s/%s" % (path[1:], name))
        if inst is not None:
            return inst
        path = path[:path.rindex('/')]
    return component.getUtility(ISkinObject, name=name)
