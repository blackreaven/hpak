#
# create_links.sh - a simple script to create sym links for aircrack-ng
#
# Written by @Hypsurus
#

AIRCRACK_PATH="/opt/pentest/wireless-attacks/aircrack-ng/"
BINS="airbase-ng  aircrack-ng  airdecap-ng  airdecloak-ng  aireplay-ng  airodump-ng  airserv-ng  airtun-ng  makeivs-ng  packetforge-ng"

# Here is work
for bin in $BINS;do
  ln -s "${AIRCRACK_PATH}/src/${bin}" "/usr/local/bin/${bin}"
done;

# Airmon-ng
ln -s "${AIRCRACK_PATH}/scripts/airmon-ng" /usr/local/bin/airmon-ng
chmod +x /usr/local/bin/airmon-ng
