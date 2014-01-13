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

from flask import jsonify

class ErrorHandler:
    class __impl:
        status = 0
        message = ""

    __instance = None

    def __init__(self):
        if ErrorHandler.__instance is None:
            ErrorHandler.__instance = ErrorHandler.__impl()

        self.__dict__['_Singleton__instance'] = ErrorHandler.__instance

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value) 

    def __str__(self):
        message = {
                'status': self.status,
                'message': self.message,
        }
        resp = jsonify(message)
        resp.status_code = self.status

        return resp
