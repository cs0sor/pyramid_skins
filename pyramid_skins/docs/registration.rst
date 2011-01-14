Registration
============

In the course of this narrative we will demonstrate different usage
scenarios. The example test setup contains the following files::

  ./skins/index.pt
  ./skins/main_template.pt
  ./skins/images/logo.png
  ./skins/about/index.pt
  ./skins/about/images/logo.png

         ↳ mount point

.. -> output

  >>> import os
  >>> from pyramid_skins import tests
  >>> for filename in output.split('\n'):
  ...     if filename.lstrip().startswith('.'):
  ...         assert os.lstat(
  ...             os.path.join(os.path.dirname(tests.__file__), filename.strip())) \
  ...             is not None

To explain this setup, imagine that the ``index.pt`` template
represents some page in the site (e.g. the *front page*); it uses
``main_template.pt`` as the :term:`o-wrap` template. The ``about``
directory represents some editorial about-section where
``about/index.pt`` is the index page. This section provides its own
logo.

We begin by registering the directory. This makes the files listed
above available as skin components. The ZCML-directive ``skins`` makes
registration easy::

    <configure xmlns="http://pylonshq.com/pyramid" >
        <include package="pyramid_skins" />
        <skins path="skins" />
    </configure>

.. -> configuration

.. invisible-code-block: python

  from zope.configuration.xmlconfig import string
  _ = string("""
     <configure xmlns="http://pylonshq.com/pyramid" package="pyramid_skins.tests">
     <include package="pyramid.includes" file="meta.zcml" />
       %(configuration)s
     </configure>""".strip() % locals())

  from zope.component import getUtility
  from pyramid_skins.interfaces import ISkinObject
  getUtility(ISkinObject, name="index")

The ``path`` parameter indicates a relative path which defines the
mount point for the skin registration.

Components
##########

At this point the skin objects are available as utility
components. This is the low-level interface::

  from zope.component import getUtility
  from pyramid_skins.interfaces import ISkinObject
  index = getUtility(ISkinObject, name="index")

.. -> code

  >>> exec(code)
  >>> assert index is not None

The component name is available in the ``name`` attribute::

  index.name

.. -> expr

  >>> eval(expr)
  'index'

We now move up one layer and consider the skin components as objects.

Objects
#######

The ``SkinObject`` class itself wraps the low-level utility lookup::

  from pyramid_skins import SkinObject
  FrontPage = SkinObject("index")

.. -> code

  >>> exec(code)
  >>> FrontPage.__get__() is not None
  True

This object is a callable which will render the template to a response
(it could be an image, stylesheet or some other resource type). In the
case of templates, the first two positional arguments (if given) are
mapped to ``context`` and ``request``. These symbols are available for
use in the template.

::

  response = FrontPage(u"Hello world!")

.. -> code

The index template simply inserts the ``context`` value into the body
tag of the HTML document::

  <html>
    <body>
      Hello world!
    </body>
  </html>

.. -> output

  >>> exec(code)
  >>> response.body.replace('\n\n', '\n') == output.strip('\n')
  True
  >>> response.content_type == 'text/html'
  True
  >>> response.charset == 'UTF-8'
  True

The exact same approach works for the logo object::

  from pyramid_skins import SkinObject
  logo = SkinObject("images/logo.png")

.. -> code

Calling the ``logo`` object returns an HTTP response::

  200 OK

.. -> output

  >>> exec(code)
  >>> response = logo()
  >>> response.status == output.strip('\n')
  True
  >>> response.content_type == 'image/png'
  True
  >>> response.content_length == 2833
  True
  >>> response.charset == None
  True

  >>> exec(code)
  >>> response.headers['content-type']
  'image/png'

