#!/usr/bin/env bash
#
# patch_python_version.sh - fix env python to env python2
#
# Written by @Hypsurus 
#

PATH="/opt/pentest/vulnerability-analysis/sqlmap/"
/bin/sed -i "s/env python/env python2/g" "$PATH/sqlmap.py"

