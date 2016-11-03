#!/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/bin/python
#
# The Python Imaging Library.
# $Id$
#
# a utility to identify image files
#
# this script identifies image files, extracting size and
# pixel mode information for known file formats.  Note that
# you don't need the PIL C extension to use this module.
#
# History:
# 0.0 1995-09-01 fl   Created
# 0.1 1996-05-18 fl   Modified options, added debugging mode
# 0.2 1996-12-29 fl   Added verify mode
# 0.3 1999-06-05 fl   Don't mess up on class exceptions (1.5.2 and later)
# 0.4 2003-09-30 fl   Expand wildcards on Windows; robustness tweaks
#

from __future__ import print_function



import sys
sys.path[0:0] = [
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Plone-4.3.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.upgrade-1.3.27-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Pillow-3.3.0-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PrintingMailHost-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.async-1.7.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.minmax-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/simplejson-2.5.2-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/rwproperty-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.keyreference-3.6.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/five.intid-1.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.z3monitor-0.8.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.monitor-0.3.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.async-1.5.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/setuptools-20.9.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/src/eea.pdf',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Zope2-2.13.24-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ZCatalog-2.13.27-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ResourceRegistries-2.2.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PortalTransforms-2.1.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PlonePAS-5.0.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.MimetypesRegistry-2.0.10-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.GenericSetup-1.8.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFQuickInstallerTool-3.0.13-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFFormController-3.0.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFEditions-2.2.21-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFDiffTool-2.2.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFCore-2.2.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.contentmigration-2.1.13-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.Archetypes-1.9.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFPlone-4.3.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Acquisition-2.13.9-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.interface-3.6.7-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.component-3.9.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/transaction-1.1.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.portlets-2.5.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.folder-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.session-3.5.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.portlets-2.2.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/borg.localrole-3.0.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/wicked-1.1.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.theming-1.1.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.openid-2.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.iterate-2.1.17-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.dexterity-2.0.18-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.caching-1.1.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFPlacefulWorkflow-1.5.13-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/ZODB3-3.10.5-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.schema-4.2.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/mock-1.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.appsetup-3.14.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.ngi-2.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.bforest-1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Twisted-16.5.0-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.twist-1.3.1-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.dict-1.2.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.queue-1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/uuid-1.30-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/pytz-2013b-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/src/eea.downloads',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/src/eea.converter',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.BTreeFolder2-2.13.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.security-3.7.4-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.proxy-3.6.1-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.container-3.11.2-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.browser-1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zLOG-2.11.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/initgroups-2.13.0-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/docutils-0.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/ZConfig-2.9.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Record-2.13.0-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Persistence-2.13.2-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/MultiMapping-2.13.0-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Missing-2.13.1-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/ExtensionClass-2.13.2-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/DocumentTemplate-2.13.2-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/DateTime-3.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/AccessControl-3.0.11-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.registry-1.2.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Markdown-2.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.intelligenttext-2.1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.protect-2.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.memoize-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.i18n-2.0.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.formlib-4.3.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.uuid-1.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.folder-1.0.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.validation-2.0.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.statusmessages-4.1.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PlacelessTranslationService-2.0.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.Marshall-2.1.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFDefault-2.2.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFCalendar-2.2.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plonetheme.sunburst-1.4.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plonetheme.classic-1.3.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.theme-2.1.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.registry-1.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.portlet.static-2.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.portlet.collection-2.1.10-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.locking-2.0.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.fieldsets-2.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.contentrules-2.0.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.browserlayer-2.1.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.batching-1.0.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.workflow-2.1.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.vocabularies-2.1.24-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.viewletmanager-2.0.10-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.uuid-1.1.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.users-1.2.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.search-1.1.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.redirector-1.2.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.locales-4.3.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.linkintegrity-1.5.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.layout-2.3.15-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.jquerytools-1.8.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.jquery-1.7.2.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.i18n-2.0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.form-2.2.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.discussion-2.2.18-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.customerize-1.2.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.controlpanel-2.3.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.contentrules-3.0.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.contentmenu-2.0.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.contentlisting-1.0.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.content-2.1.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.collection-1.0.13-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.blob-1.5.17-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/five.customerize-1.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/archetypes.referencebrowserwidget-2.5.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/archetypes.querywidget-1.1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.TinyMCE-1.3.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PloneLanguageTool-3.2.8-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.PasswordResetTool-2.0.19-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ExternalEditor-1.1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ExtendedPathIndex-3.1.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFDynamicViewFTI-4.1.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.CMFActionIcons-2.1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ATContentTypes-2.1.19-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/feedparser-5.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/five.formlib-1.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.resourceeditor-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.resource-1.0.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.transformchain-1.2.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.subrequest-1.7.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/lxml-2.3.6-py2.7-linux-x86_64.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/roman-1.4.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/diazo-1.1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.openid-2.0.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/z3c.form-3.2.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.supermodel-1.2.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.autoform-1.6.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.z3cform-0.7.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.schemaeditor-1.3.11-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.rfc822-1.1.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.namedfile-3.0.9-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.formwidget.namedfile-1.0.15-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.dexterity-2.2.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.behavior-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.textfield-1.2.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/collective.z3cform.datetimewidget-1.2.7-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.cachepurging-1.0.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.caching-1.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/python_dateutil-2.4.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.session-3.9.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/incremental-16.10.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/constantly-15.1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/collective.monkeypatcher-1.1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.stringinterp-1.0.14-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/PyPDF2-1.26.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/kv-0.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Unidecode-0.4.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/python_gettext-1.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.form-4.0.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zc.buildout-2.5.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.imaging-1.0.13-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.app.querystring-1.2.10-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.scale-1.4.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/archetypes.schemaextender-2.1.6-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.content-3.5.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.outputfilters-1.15.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/Products.ATReferenceBrowserWidget-3.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.globalrequest-1.2-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/future-0.13.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/six-1.10.0-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/experimental.cssselect-0.3-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.app.file-3.6.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/plone.alterego-1.0.1-py2.7.egg',
  '/home/irina/Plone/uvc.pdfprinter/buildouts/plone4/eggs/zope.dublincore-3.7.0-py2.7.egg',
  ]


import getopt
import glob
import logging
import sys

from PIL import Image

if len(sys.argv) == 1:
    print("PIL File 0.4/2003-09-30 -- identify image files")
    print("Usage: pilfile [option] files...")
    print("Options:")
    print("  -f  list supported file formats")
    print("  -i  show associated info and tile data")
    print("  -v  verify file headers")
    print("  -q  quiet, don't warn for unidentified/missing/broken files")
    sys.exit(1)

try:
    opt, args = getopt.getopt(sys.argv[1:], "fqivD")
except getopt.error as v:
    print(v)
    sys.exit(1)

verbose = quiet = verify = 0
logging_level = "WARNING"

for o, a in opt:
    if o == "-f":
        Image.init()
        id = sorted(Image.ID)
        print("Supported formats:")
        for i in id:
            print(i, end=' ')
        sys.exit(1)
    elif o == "-i":
        verbose = 1
    elif o == "-q":
        quiet = 1
    elif o == "-v":
        verify = 1
    elif o == "-D":
        logging_level = "DEBUG"

logging.basicConfig(level=logging_level)


def globfix(files):
    # expand wildcards where necessary
    if sys.platform == "win32":
        out = []
        for file in files:
            if glob.has_magic(file):
                out.extend(glob.glob(file))
            else:
                out.append(file)
        return out
    return files

for file in globfix(args):
    try:
        im = Image.open(file)
        print("%s:" % file, im.format, "%dx%d" % im.size, im.mode, end=' ')
        if verbose:
            print(im.info, im.tile, end=' ')
        print()
        if verify:
            try:
                im.verify()
            except:
                if not quiet:
                    print("failed to verify image", end=' ')
                    print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
    except IOError as v:
        if not quiet:
            print(file, "failed:", v)
    except:
        import traceback
        if not quiet:
            print(file, "failed:", "unexpected error")
            traceback.print_exc(file=sys.stdout)
