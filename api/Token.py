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

import requests, json
from flask import Flask, request, jsonify, abort, make_response
from flask.ext.classy import FlaskView, route
from api import *
from api.Authenticate import *

class Token(FlaskView,object):
    def __init__(self):
        self.tokenid = unicode('')
        self.valid   = False

    @route('/tokens', methods=['POST'])
    @requires_auth
    def auth(self):
        return make_response(jsonify( { 'access' : { 'token': { 'id': self.tokenid } } } ), 200)

    @route('/tokens/<string:tokenid>', methods=['GET'])
    @validate_token
    def validate(self, tokenid):
        self.tokenid = tokenid
        if self.valid:
            return make_response(jsonify( {} ), 200)
        else:
            return make_response(jsonify( {} ), 203)

    @route('/tokens/<string:tokenid>', methods=['DELETE'])
    def logout(self, tokenid):
        try:
            oauth = Auth()
            rval = oauth.logout(tokenid)
        except KeyError:
            abort(400)

        if rval:
            return make_response(jsonify( {} ), 200)
        else:
            return make_response(jsonify( {} ), 202)
