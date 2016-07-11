#
# remove_links.sh - a simple script to remove links.
#
# Written by @Hypsurus
#

BINS="airbase-ng  aircrack-ng  airdecap-ng  airdecloak-ng  aireplay-ng  airodump-ng  airserv-ng  airtun-ng  makeivs-ng  packetforge-ng airmon-ng"

# Here is work
for bin in $BINS;do
  rm "/usr/local/bin/${bin}"
done;
