#
# archlinux_depends.sh - install depedns for the package
#
# See 'LICENSE' for details.
#


PACKAGE_MANAGER="pacman"
INSTALL="--noconfirm --needed -S"
REMOVE="--noconfirm -Rns"
# Put here the packages 
PACKAGES="base-devel"


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
