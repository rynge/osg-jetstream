
/etc/dhcp/dhclient.d/osg.sh:
  file.managed:
    - source: salt://dhcp/osg.sh
    - user: root
    - group: root
    - mode: 755

