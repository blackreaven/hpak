hpak - package manager for pentesters.
----------------------------------------

Command line:

![screenshot01](https://raw.githubusercontent.com/wiki/Hypsurus/hpak/images/screenshot01.png)

Web:

![hpak_web](https://raw.githubusercontent.com/wiki/Hypsurus/hpak/images/hpak_web.png)

About
------

Hpak is a package manager for pentesters. this tool download & extract the tools into /opt/pentest and creates symlink to the script/binary in 
/usr/local/bin/,
Hpak can remove/update/reinstall the tools and install tools depends by the OS package manager or python-pip, npm etc...

Hpak helps you to install/remove any tool in fast and easy way.

TODO
------

* `list` options
* Create .gz package
* Install packages by the web-interface.

Requirements:
-------------

* Python 2.7

Tested on
-----------

* Archlinux
* Debian
* Ubuntu

#### Install this packages via your OS package manager:

* ![Debian](https://www.debian.org/logos/openlogo-50.png)  `sudo apt-get install python-pip`

* ![Archlinux](https://bbs.archlinux.org/img/avatars/29715.png?m=1254930165)  `sudo apt-get install python2-pip`


#### You can own /opt/pentest/ by running:

```bash
sudo chown USER_NAME -R /opt/pentest
```

and then you will have write access to this folder.

Installation
-------------------

`sudo setup.py install`

Create new package
-------------------------------

Please follow [this](https://github.com/Hypsurus/hpak/wiki/Create_Package) tutorial in the wiki.

or read any package in ./packages and see how it works.

Core team
----------

* @Hypsurus

Platforms
-----------

* Linux (any)
* Mac ???

Copying
========

Copyright 2016 (C) Hypsurus <hypsurus@mail.ru>
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>..
