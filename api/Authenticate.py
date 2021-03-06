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
from functools import wraps
from api import *

def authenticate(auth):
    try:
        oauth = Auth()
        rid = oauth.authenticate(auth['username'],auth['password'])
        if not rid:
            abort(401)
        else:
            token = json.loads(rid)['tokenId']
    except ValueError:
        # json bad format
        abort(400)
    except KeyError:
        # auth key does not exists
        abort(400)
    return token

def requires_auth(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        try:
            data = json.loads(request.data)
            auth = data['auth']['passwordCredentials']
        except ValueError:
            # json error, bad format
            abort(400)
        except KeyError:
            # auth key does not exists
            abort(400)

        if not auth:
            abort(401)
        self.tokenid = authenticate(auth)
        return f(self, *args, **kwargs)
    return decorated
def validate_token(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        try:
            self.tokenid = kwargs['tokenid']
            oauth = Auth()
            self.valid = oauth.validate(self.tokenid)
        except KeyError:
            abort(400)

        return f(self, *args, **kwargs)
    return decorated

