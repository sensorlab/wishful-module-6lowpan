import logging
import random
import wishful_upis as upis
import wishful_framework as wishful_module
from wishful_framework.classes import exceptions

import iperf3
from time import sleep

__author__ = "Matevz Vucnik"
__copyright__ = "Copyright (c) 2017, Jozef Stefan Instiute"
__version__ = "0.1.0"
__email__ = "matevz.vucnik@ijs.si"

@wishful_module.build_module
class SixlowpanModule(wishful_module.AgentModule):

    def __init__(self):
        super(SixlowpanModule, self).__init__()
        self.log = logging.getLogger('SixlowpanModule')

    @wishful_module.bind_function(upis.net.create_packetflow_sink)
    def create_packetflow_sink(self, port):
        self.log.debug("Starts iperf server on port {}".format(port))
        server = iperf3.Server()
        server.port = port
        server.run()
        return "Iperf server exited"

    @wishful_module.bind_function(upis.net.start_packetflow)
    def start_packetflow(self, dest_ip, port):
        self.log.debug("Start iperf client.")
        client = iperf3.Client()
        client.duration = 1
        client.server_hostname = dest_ip
        client.port = port
        for i in range(10):
            result = client.run()
            if result.error:
                sleep(1)
            else:
                break
        return result
