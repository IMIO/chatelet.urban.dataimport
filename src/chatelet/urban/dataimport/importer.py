# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from chatelet.urban.dataimport.interfaces import IChateletDataImporter


class ChateletDataImporter(AgorawinDataImporter):
    """ """

    implements(IChateletDataImporter)
