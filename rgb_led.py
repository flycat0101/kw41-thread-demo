#!/usr/bin/env python
'''
* The MIT License (MIT)
* Copyright (c) 2012 Maciej Wasilak
*
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in all
* copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
* SOFTWARE.
'''

from random import randint
import sys

from twisted.internet import reactor, task
from twisted.python import log

import txthings.coap as coap
import txthings.resource as resource

import time

try:
    from ipaddress import ip_address
except ImportError:
    sys.exit("Please update txThings: # pip install txThings --upgrade")

looptimes = 0

class Agent():

    def __init__(self, protocol):
        self.protocol = protocol

    def putResource(self):
        if sys.argv[2] == "on":
            payload = "rgb\x00r" + str(randint(100, 1000)) + "\x00g" + \
                str(randint(10, 1000)) + "\x00b" + str(randint(10, 1000)) + "\x00"
        else:
            payload = "off"
        request = coap.Message(code=coap.POST, payload=payload)
        request.opt.uri_path = ("led",)
        request.opt.content_format = coap.media_types_rev[
            'application/octet-stream']
        request.remote = (ip_address(sys.argv[1]), coap.COAP_PORT)
        d = protocol.request(request)

    def printResponse(self, response):
        print 'Response Code: ' + coap.responses[response.code]
        print 'Payload: ' + response.payload

if len(sys.argv) < 3:
    print 'Usage: $ %s <FRDM_KW24 ULA>' % sys.argv[0]
    sys.exit(1)

endpoint = resource.Endpoint(None)
protocol = coap.Coap(endpoint)
client = Agent(protocol)

reactor.listenUDP(coap.COAP_PORT, protocol, interface='::0')

while (looptimes < 5):
    client.putResource()
    time.sleep(1)
    looptimes += 1
    if sys.argv[2] == "off":
        sys.exit(1)
