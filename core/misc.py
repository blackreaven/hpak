# -*- coding: utf-8 -*-
#
# misc.py - library for the good stuff
#
# Copyright (c) 2016 hpak project.
# See 'LICENSE' for details.
#

import os
import sys
import shutil

LINUX_DIST_FILES = {"debian"    : "/etc/apt/sources.list",
									  "archlinux" : "/etc/arch-release"} 

HPAK_ROOT = "/opt/pentest/"
HPAK_PREFIX = "/usr/local"
PKGS_ROOT = "%s/packages/" % (HPAK_ROOT)

from core.db import hpakDB

class misc:
	""" Functions to get is right """
	def __init__(self):
		pass

	@staticmethod
	def is_root():
		if os.getuid() == 0:
			return True
		return False

	@staticmethod
	def print_info(msg):
		sys.stdout.write("\033[01;34m✓\033[00m\033[01;01m %s\033[00m\n" % (msg.encode('utf-8')))

	@staticmethod
	def print_warning(msg):
		sys.stdout.write("\033[01;35m☢\033[00m\033[01;01m %s\033[00m\n" % (msg.encode('utf-8')))

	@staticmethod
	def print_success(msg):
		sys.stdout.write("\033[01;32m✓\033[00m\033[01;01m %s\033[00m\n" % (msg.encode('utf-8')))

	@staticmethod
	def print_error(msg, exit):
		sys.stdout.write("\033[01;31m❄\033[00m\033[01;01m %s\033[00m\n" % (msg.encode('utf-8')))
		if exit: sys.exit(0)

	@staticmethod
	def detect_os():
		if "linux" in sys.platform:
			for dist in LINUX_DIST_FILES:
				if os.path.exists(LINUX_DIST_FILES[dist]):
					return dist
			if "win" in sys.platform:
				misc.print_error("hpak has no support for windows!", True)

	@staticmethod
	# Create new package wizard
	def create(pkg_name):
		misc.print_info("Welcome to hpak package create wizard.")
		misc.print_info("Please follow the wizard to create the \'%s\' package." % (pkg_name))
		pkg_path = "%s%s/%s.json" % (PKGS_ROOT, pkg_name, pkg_name)	

		try:
			shutil.copytree("./tools/package.example/", "%s%s/" % (PKGS_ROOT,pkg_name))
			os.rename("%s%s/package_example.json" % (PKGS_ROOT,pkg_name), pkg_path)
		except OSError:
			misc.print_error("Package already exists.", True)

		# Set variables
		h = hpakDB(pkg_name)
		h.set_value("package", pkg_name)
		
		version = raw_input("\033[01;34m❄ Version (1.0) : \033[00m") or "1.0"
		license = raw_input("\033[01;34m❄ License (GPLv3) : \033[00m") or "GPLv3"
		url = raw_input("\033[01;34m❄ URL (homepage) : \033[00m")
		source = raw_input("\033[01;34m❄ Source (archive url) : \033[00m")

		h.set_value("version", version)
		h.set_value("license", license)
		h.set_value("url", url)
		h.set_value("source", source)

		depScript = raw_input("\033[01;34m❄ Package has depends ? (yes/no) : \033[00m")
		h.set_value("depScript", depScript)

		misc.print_info("Please edit the package json file with install/remove commands.")
		misc.print_info("You can add logo/screenshot for the website interface.")
		misc.print_success("Package \'%s\' created!" % (pkg_name))
		
