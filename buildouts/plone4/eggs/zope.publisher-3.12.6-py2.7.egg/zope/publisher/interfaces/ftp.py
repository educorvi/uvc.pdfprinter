##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Virtual File System interfaces for the publisher.
"""

__docformat__ = "reStructuredText"

from zope.interface import Interface

from zope.publisher.interfaces import IPublishTraverse
from zope.publisher.interfaces import IRequest
from zope.publisher.interfaces import IView

class IFTPRequest(IRequest):
    """FTP Request
    """

class IFTPView(IView):
    """FTP View"""

class IFTPCredentials(Interface):

    def _authUserPW():
        """Return (login, password) if there are basic credentials;
        return None if there aren't."""

    def unauthorized(challenge):
        """Cause a FTP-based unautorized error message"""


class IFTPPublisher(IPublishTraverse):
    """FTP Publisher"""
