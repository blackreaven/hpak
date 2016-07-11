#
# mac_depends.sh - Install commands for Ma* OS
#
# See 'LICENSE' for details.
#

# I DONE HAVE MAC OS!
# SO I CANT CODE THIS SCRIPT.
#

PACKAGE_MANAGER=""
INSTALL=""
REMOVE=""
# Put here the packages 
PACKAGES=""


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
