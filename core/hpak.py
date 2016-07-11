# -*- coding: utf-8 -*-
#
# hpak.py - the main hpak module.
#
# Copyright (c) 2016 hpak project.
# See 'LICENSE' for details.
#

import sys
import json
import os
import subprocess
from misc import misc
from misc import HPAK_ROOT
from misc import HPAK_PREFIX
from misc import PKGS_ROOT
from download import download
from extractor import Extractor
from core.db import hpakDB

class Hpak(object):
	""" This package read install/uninstall actions. """
	def __init__(self, pkg_name):
		self.pkg = "%s/%s/%s.json" % (PKGS_ROOT, pkg_name, pkg_name)
		self.pkg_name = pkg_name
		self.options = None

		try:
			with open(self.pkg, 'r') as api:
				self.options = json.load(api)
				self.pkg_path = "%s%s" % (HPAK_ROOT, self.options['dir'])
				self.options['dir'] = self.options['dir'].encode('utf-8')

				# Replace some variables in the PKG file.
				self.options['install'] = self.options['install'].replace("$PKG_DIR", "%s/%s" % (self.pkg_path, self.pkg_name)) 
				self.options['install'] = self.options['install'].replace("$SCRIPTS_DIR", "%s/%s/scripts/" % (PKGS_ROOT,self.pkg_name)) 
				self.options['install'] = self.options['install'].replace("$PREFIX", HPAK_PREFIX) 
				self.options['remove'] = self.options['remove'].replace("$PKG_DIR", "%s/%s" % (self.pkg_path, self.pkg_name)) 
				self.options['remove'] = self.options['remove'].replace("$SCRIPTS_DIR", "%s/%s/scripts/" % (PKGS_ROOT, self.pkg_name)) 
				self.options['remove'] = self.options['remove'].replace("$PREFIX", HPAK_PREFIX) 
		except IOError:
			misc.print_error("No such package.", True)
	
	# Prepare installation, Create root directory for hpak
	def prepare_install(self):
		misc.print_info("Installing \'%s-%s\' ..." % (self.pkg_name, self.options['version']))

		if not misc.is_root():
			misc.print_error("Please run as root.", True)

		if not os.path.exists(HPAK_ROOT):
			os.mkdir(HPAK_ROOT)
		elif not os.path.exists("%s/%s" %(HPAK_ROOT, self.options['dir']) ):
			os.mkdir("%s/%s" %(HPAK_ROOT, self.options['dir']) )

	# Install depends
	def install_dep(self):
		misc.print_info("Installing depends...")
		os = misc.detect_os()
		try:
			if self.options['depScript'] == "yes":
				Cmd = "bash %s/%s/scripts/%s_depends.sh install" % (PKGS_ROOT, self.pkg_name, os)
				subprocess.Popen(Cmd, shell=True).wait()
		except KeyError:
			pass

	# Install package
	def install(self):
		# Check if package installed
		db = hpakDB(self.pkg_name)
		if db.get_value("status") == "installed":
			misc.print_error("%s - already installed!" % (self.pkg_name), False)
			return
							
		self.prepare_install()
		dl = download(self.options['source'], self.pkg_path, self.pkg_name)
		dl.get()
		
		# Extracting the file.
		e =	Extractor(self.options)
		e.extract()

		# Install depends
		self.install_dep()

		Cmds = self.options['install'].split(',')
		for cmd in Cmds:
			subprocess.Popen(cmd, shell=True).wait()

		# Verify package installed.
		if os.path.exists("%s/%s" % (HPAK_ROOT, self.options['dir'])):
			db = hpakDB(self.pkg_name)
			db.set_value("status", "installed")
			misc.print_success("%s installed." % (self.pkg_name))
		else:
			misc.print_error("%s-%s NOT installed, please try again." % (self.pkg_name, self.options['version']), True) 

	# Remove & register package
	def remove(self):
		misc.print_info("Removing %s-%s ..." % (self.pkg_name, self.options['version']))

		db = hpakDB(self.pkg_name)
		if db.get_value("status") == "removed":
			misc.print_error("%s - not installed" % (self.pkg_name), False)
			return

		os = misc.detect_os()
		try:
			if self.options['depScript'] == "yes":
				Cmd = "bash %s/%s/scripts/%s_depends.sh remove" % (PKGS_ROOT, self.pkg_name, os)
				subprocess.Popen(Cmd, shell=True).wait()
		except KeyError:
			pass

		# Running remove commands
		Cmds = self.options['remove'].split(',')
		for cmd in Cmds:
			subprocess.Popen(cmd, shell=True).wait()

		db = hpakDB(self.pkg_name)
		db.set_value("status", "removed")

		misc.print_success("%s has been removed." % (self.pkg_name))

	# Show package information
	def info(self):
		for opt in self.options:
			key = opt
			if key == "screenshot":
				key = "image"
			elif key == "description":
				key = "desc"
			elif key == "depScript":
				key = "script"
			print("\033[01;32m%s\033[00m\t:\t\033[01;33m%s\033[00m" % ( key.title().encode('utf-8'), 
			self.options[opt].encode('utf-8')) )

# Starts here
ARGS = ['install', 'info', 'remove', 'search', 'create', 'version', 'help']
USAGE_MSG = '''\033[00mUsage: %s [option] [pkg] [pkg] ...

Options:
	install - Install packages.
	remove  - Remove packages.
	info    - Get package information.
	search  - Search package name or text in package description.
	version - Show version, author and more info.
	help    - Show this.

Copyright 2016 (c) hpak project
Full documentation at: <https://github.com/Hypsurus/hpak>\033[00m''' % (sys.argv[0])

def print_usage(exit):
	print(USAGE_MSG);
	if exit: sys.exit(0)

# Parse command line arguments
def parse_cli(argv):
	flag = 0
	argv.pop(0) # remove file name
	packages = []

	for arg in ARGS:
		if arg == argv[0]:
			flag +=1
			if arg == "search":
				h = hpakDB("None")
				h.search(argv[1])
				sys.exit(0)
			elif arg == "create":
				misc.create(argv[1])
			else:
				packages = argv[1:]
			
	if not packages:
		misc.print_error("no package specified or missing option.", True)

	if flag == 0:
		misc.print_error("%s - no such option." % (argv[0]), True)

	for package in packages:
		h = Hpak(package)
		if argv[0] == "install":
			h.install()
		elif argv[0] == "remove":
			h.remove()
		elif argv[0] == "info":
			h.info()

def main():
	if len(sys.argv) < 2:
		print_usage(True)

	parse_cli(sys.argv)	
