""" Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'uvc.pdfprinter'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description="uvc pdf printer",
      long_description=(open("README.txt").read() + "\n" +
                        open(os.path.join("docs", "HISTORY.txt")).read()),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        ],
      keywords='plone zope python',
      author='Eau de Web',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.pdf > 4.9',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
