#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Copyright(c) 2019 Nippon Telegraph and Telephone Corporation
# Filename: EmCgwshPPPMerge.py

'''
Individual scenario for merging PPP in Cgwsh service
'''
import json
from lxml import etree
import GlobalModule
from EmCommonLog import decorater_log
from EmCgwshServiceFlavor import EmCgwshServiceFlavor
from EmCgwshServiceBase import EmCgwshServiceBase


class EmCgwshPPPMerge(EmCgwshServiceFlavor, EmCgwshServiceBase):
    '''
    Class for merging PPP in Cgwsh service
    '''


    @decorater_log
    def __init__(self):
        '''
        Costructor
        '''
        super(EmCgwshPPPMerge, self).__init__()
        super(EmCgwshServiceFlavor, self).__init__()

        self.service = GlobalModule.SERVICE_CGWSH_PPP_SESSION
        self.order_type = GlobalModule.ORDER_MERGE

        self._xml_ns = "{%s}" % GlobalModule.EM_NAME_SPACES[self.service]

        self._scenario_name = "CgwshPPPMerge"

    @decorater_log
    def _creating_json(self, device_message):
        '''
        EC Message(XML) devided into each device is converted to JSON.
        Argument:
            device_message:  message for each device
        Return value:
            device_json_message: JSON message
        '''
        xml_elm = etree.fromstring(device_message)

        GlobalModule.EM_LOGGER.debug(
            "device_message = %s", etree.tostring(xml_elm, pretty_print=True))

        device_json_message = self._get_nvr_ppp_info(xml_elm)

        GlobalModule.EM_LOGGER.debug(
            "device__json_message = %s", device_json_message)

        return json.dumps(device_json_message)
