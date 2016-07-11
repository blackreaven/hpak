# *-* coding: utf-8 *-*
#
# db.py - Manage local database using JSON files.
#
# Copyright (c) 2016 hpak project.
# See 'LICENSE' for details.
#

from misc import misc
from misc import PKGS_ROOT
import os

class Test(object):
	""" Run tests for hpal """
	def __init__(self):
		self.ready = None
		misc.detect_os()

	"""
		Tests if user execute setup.py install
	"""
	def run(self): 
		if not os.path.exists(PKGS_ROOT):
			misc.print_error("Please run \'setup.py install\' to get started.", True)


