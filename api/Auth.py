#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    AuthCon
    ------------

    AuthCon is a RESTful API Python connector to OpenAM.
    
    :copyright:     (c) 2014 by Alvaro Soto
    :license:       GPL v2, see LICENSE for more details.
    :contact info:  http://headup.ws / alsotoes@gmail.com
"""

__version__ = "0.0.1"

#

import requests, json, ConfigParser, os
from urllib2 import HTTPError
from api.helpers import ErrorHandler
from flask import Flask, request

class Auth():
    config = None

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read("config/authcon.cfg")

    def __del__(self):
        pass

    def authenticate(self, username, password):
        url = self.config.get( "openam", "auth" )
        headers = { 'X-OpenAM-Username': username, 'X-OpenAM-Password': password, 'Content-Type': 'application/json' }

        try:
            r = requests.post(url, headers=headers)
        except HTTPError:
            pass

        if r.status_code == requests.codes.ok :
            return r.text
        else:
            errorHandler = ErrorHandler()
            errorHandler.status = r.status_code
            errorHandler.message = r.text
            return False

    def validate(self, tokenid):
        url = self.config.get( "openam", "validate" )
        payload = 'tokenid=' + tokenid
        headers = { 'Content-Type' : 'text/plain; charset=utf-8' }

        try:
            r = requests.post(url+'?'+payload, headers=headers)
        except HTTPError:
            pass

        if r.status_code == requests.codes.ok and 'boolean=true' == (r.text).strip():
            return True
        else:
            errorHandler = ErrorHandler()
            errorHandler.status = r.status_code
            errorHandler.message = r.text
            return False

    def logout(self, tokenid):
        url = self.config.get( "openam", "logout" )
        payload = 'subjectid=' + tokenid
        headers = { 'Content-Type' : 'text/plain; charset=utf-8' }

        try:
            r = requests.post(url+'?'+payload, headers=headers)
        except HTTPError:
            pass

        if r.status_code == requests.codes.ok:
            return True
        else:
            errorHandler = ErrorHandler()
            errorHandler.status = r.status_code
            errorHandler.message = r.text
            return False
