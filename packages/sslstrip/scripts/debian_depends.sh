#
#  ubuntu_depends.sh - install depends for ubuntu and ubuntu based .
#
# See 'LICENSE' for details.
#


PACKAGE_MANAGER="apt-get"
INSTALL="--assume-yes install"
REMOVE="--assume-yes purge --autoremove"
# Put here the packages 
PACKAGES="pyopenssl"


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
