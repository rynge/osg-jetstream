
/etc/resolv.conf:
  file.managed:
    - source: salt://resolv/resolv.conf
    - user: root
    - group: root
    - mode: 644

/etc/hosts:
  file.managed:
    - source: salt://resolv/hosts
    - user: root
    - group: root
    - mode: 644

