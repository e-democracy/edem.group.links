# coding=utf-8
from zope.interface.interface import Interface
from zope.schema import Text

class IChangeLinks(Interface):
    linksText = Text(title=u'Text',
        description=u'The links that appear in the Links tab.',
        required = False)
