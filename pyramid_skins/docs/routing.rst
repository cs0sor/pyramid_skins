.. _framework-integration:

Routing
=======

The package comes with support for routing URLs to skin objects. This
works with resources -- images, stylesheets and other static files --
and templates (these are rendered into a response).

For BFG to render the skin objects, we must register views such that
the router can publish them. The benefit is that we can reuse the
``view`` directive and even protect the views with permissions.

Adding views
############

To expose the contents of a skin directory as *views*, we can insert a
``view`` registration directive into the ``skins`` directive::

  <skins path="skins">
     <view />
  </skins>

.. -> configuration

  >>> from zope.configuration.xmlconfig import string
  >>> _ = string("""
  ... <configure xmlns="http://pylonshq.com/pyramid" package="pyramid_skins.tests">
  ...   <include package="pyramid.includes" file="meta.zcml" />
  ...   <include package="pyramid_skins" />
  ...   %(configuration)s
  ... </configure>""".strip() % locals())
  >>> from pyramid.view import render_view
  >>> from pyramid.testing import DummyRequest
  >>> render = render_view('Hello world!', DummyRequest(), name="") 
  >>> print render_view('Hello world!', DummyRequest(), name="index")
  <html>
    <body>
      Hello world!
    </body>
  </html>

