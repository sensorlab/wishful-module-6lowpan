import logging
import random
import wishful_upis as upis
import wishful_framework as wishful_module
from wishful_framework.classes import exceptions

__author__ = "Matevz Vucnik"
__copyright__ = "Copyright (c) 2017, Jozef Stefan Instiute"
__version__ = "0.1.0"
__email__ = "matevz.vucnik@ijs.si"

@wishful_module.build_module
class SixlowpanModule(wishful_module.AgentModule):

    def __init__(self, service, serial):
        super(SixlowpanModule, self).__init__()
        self.log = logging.getLogger('SixlowpanModule')

    @wishful_module.bind_function(upis.radio.get_measurements)
    def get_measurements(self, params):
        return {'hello':params[0]}

    # TODO: Implement real 6LoWPAN UPIs
