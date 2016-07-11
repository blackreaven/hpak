# *-* coding: utf-8 *-*
#
# db.py - Manage local database using JSON files.
#
# Copyright (c) 2016 hpak project.
# See 'LICENSE' for details.
#


from misc import misc
from misc import HPAK_ROOT
import tarfile
import zipfile
import os

class Extractor(object):
	""" Extract archive files."""

	def __init__(self, options):
		self.options = options
		self.pkg_path = "%s/%s" % (HPAK_ROOT, self.options['dir'])
		self.file_name = self.options['source'].split('/')[-1]

	def extract(self):
		if self.file_name.endswith('.zip'):
			self.unzip()
		elif self.file_name.endswith('gz'):
			self.untar()

	def unzip(self):
		base_dir = None
		zip = zipfile.ZipFile("/tmp/%s" % (self.file_name))

		for name in zip.namelist():
			base_dir = name
			break		
		zip.extractall(path=self.pkg_path)
		misc.print_info("Extracting into \'%s\' ..." % (base_dir))

		base_dir = "%s/%s" % (self.pkg_path, base_dir)
		new_base_dir = "%s/%s" % (self.pkg_path, self.options['package'])
		os.rename(base_dir, new_base_dir)
		os.remove("/tmp/%s" % (self.file_name))

	def untar(self):
		base_dir = None
		tar = tarfile.open("/tmp/%s" % (self.file_name)) 

		for name in tar.members:
			base_dir = name.name
			break

		tar.extractall(path=self.pkg_path)
		misc.print_info("Extracting into \'%s\' ..." % (base_dir))
		
		base_dir = "%s/%s" % (self.pkg_path, base_dir)
		new_base_dir = "%s/%s" % (self.pkg_path, self.options['package'])
		os.rename(base_dir, new_base_dir)
		os.remove("/tmp/%s" % (self.file_name))

