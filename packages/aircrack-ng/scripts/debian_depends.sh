#
# depends_archlinux.sh - install depedns for the package
#
# Copyright(c) 2016 by @Hypsurus
#
# See 'LICENSE' for details.
#


PACKAGE_MANAGER="apt-get"
INSTALL="-y install"
REMOVE="-y --purge autoremove"
PACKAGES="libnl-3-dev libssl-dev build-essential pkg-config libnl-genl-3-dev ethtool"


# The real work happens here.
install() {
  eval "${PACKAGE_MANAGER} ${INSTALL} ${PACKAGES}"
}

remove() {
  eval "${PACKAGE_MANAGER} ${REMOVE} ${PACKAGES}"
}

# Command line 
if [[ $1 == "install" ]];then
  install 
elif [[ $1 == "remove" ]];then 
  remove
fi
