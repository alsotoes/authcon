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

import logging, ConfigParser, sys, re, ast, json, pprint
from flask import Flask, request, jsonify, abort, make_response
from flask.ext.classy import FlaskView, route
from api.helpers import *
from api import *

__api_version__ = 'v1.0'
authcon = Flask(__name__)
Token.register(authcon, route_base='/' + __api_version__)

##########################

@authcon.errorhandler(400)
def not_found(error=None):
    return make_response(jsonify( { 'message': "The request cannot be fulfilled due to bad syntax." } ), 400)
        
@authcon.errorhandler(401)
def not_found(error=None):
    return make_response(jsonify( { 'message': "Unauthorized." } ), 401)
        
@authcon.errorhandler(404)
def bad_request(error=None):
    return make_response(jsonify( { 'message': 'Not Found: ' + request.url } ), 404)

##########################

if __name__ == "__main__":
    authcon.run( host='0.0.0.0', port=5000, debug=False )
