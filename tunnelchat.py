#!/usr/bin/env python
"""
TODO: Document me
"""

__date__ = "$14-Apr-2010 00:59:49$"

import sleekxmpp

class TunnelChat(sleekxmpp.ClientXMPP):

    def __init__(self, jid, password, callback_object):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", callback_object.session_start)
        self.add_event_handler("message", callback_object.incoming_message)
        self.registerPlugin('xep_0004')
        self.registerPlugin('xep_0030')
        self.registerPlugin('xep_0060')
        self.registerPlugin('xep_0199')
    
if __name__ == "__main__":
    chat = TunnelChat("test@localhost", "test")
    if chat.connect(("localhost", 5222)):
        chat.process(threaded=True)
        print("Connected")
    else:
        print("Unable to connect")
