# -*- coding: utf-8 -*-

import os
from . import cgi


class PearCGI(object):

    def __init__(self):
        self.param = None

    def getMethod(self):
        methodName = os.environ['REQUEST_METHOD']
        return methodName

    def getParam(self):
        self.param = cgi.FieldStorage()
        return self.param

    def getValue(self, valueName):
        value = self.param.getvalue(valueName)
        return value

    def isValue(self, value):
        if not value:
            return False
        else:
            return True

if __name__ == '__main__':
    cgiObj = PearCGI()
