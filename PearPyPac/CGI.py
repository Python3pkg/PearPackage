# -*- coding: utf-8 -*-

import os
import cgi


class PearCGI(object):

	def __init__(self):
		return

	def isMethodPOST(self):
		if(os.environ["REQUEST_METHOD"] == "POST"):
			return True
		else:
			return False

	def isMethodGET(self):
		if(os.environ["REQUEST_METHOD"] == "GET"):
			return True
		else:
			return False

	def getParameter(self):
		param = cgi.FieldStorage()
		return param

