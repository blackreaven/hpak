#!/usr/bin/env python2
# 
# setup.py - setup script
#
#  This file is part of hpak. 
#
# Copyright (c) 2016 Hypsurus <hypsurus@mail.ru>.
#
#  See 'LICENSE' for details.
#

import shutil
import os
from setuptools import setup, find_packages
from setuptools.command.install import install
from core.misc import HPAK_ROOT
from core.misc import PKGS_ROOT

version = '1.0'

class Install(install):
  def run(self):
		install.run(self)
		if not os.path.exists(HPAK_ROOT):
			os.mkdir(HPAK_ROOT)
		shutil.copytree("./packages", "%s/packages/" % (HPAK_ROOT))
				
setup(
    name='hpak',
    version=version,
    description='package manager for pentesters.',
    author='Hypsurus',
    author_email='hypsurus@mail.ru',
    license='GPL',
    keywords=['pentest', 'command line', 'cli'],
    url='https://github.com/Hypsurus/hpak',
    packages=find_packages(),
		cmdclass = {'install' : Install},
    entry_points={
        'console_scripts': [
            'hpak=core.hpak:main'
        ],
    }
)
