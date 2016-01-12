# -*- coding: utf-8; -*-

from httpolice.common import RFC, UpgradeToken
from httpolice.known.base import KnownDict


known = KnownDict([
 {'_': UpgradeToken(u'HTTP'),
  '_citations': [RFC(7230, section=(2, 6))],
  '_title': 'Hypertext Transfer Protocol'},
 {'_': UpgradeToken(u'TLS'),
  '_citations': [RFC(2817)],
  '_title': 'Transport Layer Security'},
 {'_': UpgradeToken(u'WebSocket'),
  '_citations': [RFC(6455)],
  '_title': 'The Web Socket Protocol'},
 {'_': UpgradeToken(u'h2c'),
  '_citations': [RFC(7540, section=(3, 2))],
  '_title': 'Hypertext Transfer Protocol version 2 (HTTP/2)'}
])