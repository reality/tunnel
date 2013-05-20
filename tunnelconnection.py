#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$14-Apr-2010 00:59:49$"

import sleekxmpp

class TunnelConnection(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, start_handler, message_handler):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

        self.start_handler = start_handler
        self.message_handler = message_handler
        
        # I don't remember what these do
        self.registerPlugin('xep_0004')
        self.registerPlugin('xep_0030')
        self.registerPlugin('xep_0060')
        self.registerPlugin('xep_0199')

    def start(self, event):
        self.send_presence()
        self.get_roster()
        self.start_handler(event)

    def message(self, msg):
        self.message_handler(msg)
