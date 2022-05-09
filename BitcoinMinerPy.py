import time
import json
import pprint
import hashlib
import struct
import re
import base64
import sys
from multiprocessing import Process
import http.client

ERR_SLEEP = 15
MAX_NONCE = 1000000

settings = {}
pp = pprint.PrettyPrinter(indent=4)

class BitcoinRPC:
	OBJID = 1

	def __init__(self, host, port, username, password):
		authpair = "%s:%s" % (username, password)
		self.authhdr = "Basic %s" % (base64.b64encode(authpair))
		self.conn = httplib.HTTPConnection(host, port, False, 30)
