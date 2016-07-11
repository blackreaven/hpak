# *-* coding: utf-8 *-*
#
# db.py - Manage local database using JSON files.
#
# Copyright (c) 2016 hpak project.
# See 'LICENSE' for details.
#

import json
import os
from misc import HPAK_ROOT
from misc import PKGS_ROOT
from glob import glob

class hpakDB(object):
	"""
		Search in packages and check status of json files..
	"""
	def __init__(self, pkg_name):
		self.pkg_name = pkg_name
		self.global_db = "%s/.global_db" %(HPAK_ROOT)

	def search(self, text):
		pkgs = glob("%s/packages/*" % (HPAK_ROOT))

		for pkg in pkgs:
			name = pkg.split('/')[-1]
			pkg_name = "%s/%s.json" % (pkg, name)

			# Write database
			with open(pkg_name, "r") as api:
				options = json.load(api)
				data = options['description'].lower().encode('utf-8')
				text = text.lower()

				if text in data:
					match_text = "\033[01;31m%s\033[00m" % (text)
					data = data.replace(text, match_text)
					print("\033[01;33m✓\033[00m %s - %s" % (name, data))
				# Search words
				else:
					rate = 0
					for word in text.split():
						if word in data:
							rate += 1
					if rate > 1:
						match_text = "\033[01;31m%s\033[00m" % (text)
						data = data.replace(text, match_text)
						print("\033[01;33m✓\033[00m %s - %s" % (name, data))


	def get_value(self, KEY):
		with open("%s/%s/%s.json" % (PKGS_ROOT, self.pkg_name, self.pkg_name), "r") as api:
			options = json.load(api)
			for key in options.keys():
				if key == KEY:
					api.close()
					return options[key]

	# Set value to key
	def set_value(self, KEY, VALUE):
		options = None

		with open("%s/%s/%s.json" % (PKGS_ROOT, self.pkg_name, self.pkg_name), "r") as api:
			options = json.load(api)
			for key in options.keys():
				if key == KEY:
					options[key] = VALUE
					api.close()
	
		with open("%s/%s/%s.json" % (PKGS_ROOT, self.pkg_name, self.pkg_name), "w") as api:
			json.dump(options, api, indent=4, sort_keys=True)
			api.close()

	def close(self):
		if self.cursor:
			self.cursor.close()
