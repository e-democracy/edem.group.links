# coding=utf-8
from __future__ import absolute_import, unicode_literals
from zope.interface.interface import Interface
from zope.schema import Text


class IChangeLinks(Interface):
    related_links = Text(title='Text',
        description='The links that appear in the Links tab.',
        required=False)
