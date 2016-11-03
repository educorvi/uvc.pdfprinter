""" PDF View
"""
from logging import getLogger
from Acquisition import aq_base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from eea.pdf.themes.page.body import Body as PDFBody
from eea.pdf.themes.book.folder import Body as FolderBody


logger = getLogger('uvc.pdfprinter')
from Products.CMFPlone.utils import safe_hasattr


class Body(PDFBody):
    """ Custom PDF body
    """
    template = ViewPageTemplateFile('body.pt')

    def __call__(self, **kwargs):
        self.request.set('skipRelations', 1)
        return self.template()


