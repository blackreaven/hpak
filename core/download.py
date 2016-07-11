# *-* coding: utf-8 *-*
#
# download.py - download the package archive
# 
# Copyright (c) 2016 hpak project
# See 'LICENSE' for details.
#

import urllib2
import sys
import os
import math
from misc import misc

HTTP_USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

class download(object):
	""" Download files over HTTP/s """
	def __init__(self, url, path, pkg_name):
		self.url = url
		self.pkg_name = pkg_name
		self.file_name = self.url.split('/')[-1]
		self.cursor = None
		self.path = path

	def calc_bytes(self, size):
		if (size == 0):
			return '0B'
		size_name = ("B", "K", "M", "G", "TB", "PB", "EB", "ZB", "YB")
		i = int(math.floor(math.log(size,1024)))
		p = math.pow(1024,i)
		s = round(size/p,2)
		return '%s%s' % (s,size_name[i])

	def parse_url(self):
		if "://" in self.url:
			return self.url
		return None

	def get(self):
		self.url = self.parse_url()
		if self.url == None:
			misc.print_error("URL \'%s\' is not vaild.", True)
		
		# Build the HTTP request
		opener = urllib2.build_opener()
		opener.addheaders = [('User-Agent', HTTP_USER_AGENT)]
		try:
			self.cursor = opener.open(self.url)
		except urllib2.URLError, err:
			misc.print_error("Connection failed.", True)

		info = self.cursor.info()
		
		try:	
			file_size = "/%d" % (int(info.getheaders('Content-Length')[0]))
		except IndexError:
			file_size = ""
		file_size_dl = 0

		# Skip if file already downloaded.
		if os.path.exists("/tmp/%s" %(self.file_name)):
			misc.print_info("Found \'%s\' in /tmp ..." % (self.file_name))
			return

		fp = open("/tmp/%s" %(self.file_name), "wb")
		arrow = "❤"

		while True:
			sys.stdout.write("\033[01;36m✓\033[00m\033[01;01m %s - %d%s \033[01;31m%s\r\033[00m" % (self.pkg_name, 
			file_size_dl, file_size,
			arrow))

			if arrow == "❤":
				arrow = "♡"
			elif arrow == "♡":
				arrow = "❤"

			buffer = self.cursor.read(1024)
			file_size_dl += len(buffer)
			fp.write(buffer)
			if not buffer:
				break
		# End
		sys.stdout.write('\n')
		fp.close()
