"""Module for Alpari API."""
import time
import json
import logging
import threading
import requests
import ssl
import atexit
import tempfile
from des import DesKey
import base64
from collections import deque
from alpariapi.ws.client import WebsocketClient
from alpariapi.global_value import global_value
import collections
from collections import defaultdict
from urllib.parse import urlparse
from urllib.parse import parse_qs

class alpariapi(object):
  def __init__(self, set_ssid, user_agent, proxies, auto_logout):
    self.set_ssid = set_ssid
    self.user_agent = user_agent
    self.proxies = proxies
    self.session.verify = False
    self.session.trust_env = False
    self.auto_logout = auto_logout
    pass
  
  def get_token(self, account_id):
    pass
  
