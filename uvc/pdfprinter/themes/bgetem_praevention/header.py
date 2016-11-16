""" PDF Views
"""
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class Header(BrowserView):
    """ PDF Header
    """
    template = ViewPageTemplateFile('header.pt')

    def __call__(self, **kwargs):
	return self.template()
