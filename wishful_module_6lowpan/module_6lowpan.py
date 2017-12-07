import logging
import random
import wishful_upis as upis
import wishful_framework as wishful_module
from wishful_framework.classes import exceptions

import asyncio
from aiocoap import *
from time import sleep

__author__ = "Matevz Vucnik"
__copyright__ = "Copyright (c) 2017, Jozef Stefan Instiute"
__version__ = "0.1.0"
__email__ = "matevz.vucnik@ijs.si"

@wishful_module.build_module
class SixlowpanModule(wishful_module.AgentModule):
    uri = None
    run = None

    def __init__(self, uri):
        super(SixlowpanModule, self).__init__()
        self.log = logging.getLogger('SixlowpanModule')
        self.uri = uri
        self.run = asyncio.get_event_loop().run_until_complete

    @asyncio.coroutine
    def get_rssi_lqi(self):
        protocol = yield from Context.create_client_context()
        msg = Message(code=GET, uri=self.uri)
        response = yield from protocol.request(msg).response
        return response.payload

    @wishful_module.bind_function(upis.radio.get_measurements)
    def get_measurements(self, params):
        response = self.run(self.get_rssi_lqi())
        return {response.payload}
