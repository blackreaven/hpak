#!/usr/bin/env bash
#
# patch_python_version.sh - fix env python to env python2
#
# Written by @Hypsurus 
#

PATH="/opt/pentest/information-gathering/sslstrip"
/bin/sed -i "s/env python/env python2/g" "$PATH/sslstrip.py"

