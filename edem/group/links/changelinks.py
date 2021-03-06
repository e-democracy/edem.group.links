# coding=utf-8
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base.wymeditor import wym_editor_widget
from gs.content.form.base.utils import enforce_schema
from gs.group.base.form import GroupForm
from .interfaces import IChangeLinks


class ChangeLinks(GroupForm):
    pageTemplateFileName = 'browser/templates/changelinks.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, group, request):
        GroupForm.__init__(self, group, request)

    @Lazy
    def label(self):
        retval = 'Change the Links tab for %s' % self.groupInfo.name
        assert type(retval) == unicode
        return retval

    @Lazy
    def form_fields(self):
        enforce_schema(self.context, IChangeLinks)
        retval = form.Fields(IChangeLinks, render_context=True)
        retval['related_links'].custom_widget = wym_editor_widget
        return retval

    @form.action(label='Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)

        self.status = 'The Links tab on the homepage for '\
                      '<a href="%s">%s</a> has been changed.' %\
                      (self.groupInfo.relative_url(), self.groupInfo.name)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
