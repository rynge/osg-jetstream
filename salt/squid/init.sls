
squid_packages:
  pkg.installed:
    - pkgs:
      - squid

/etc/squid/squid.conf:
  file.managed:
    - source: salt://squid/squid.conf
    - user: root
    - group: root
    - mode: 644
    - template: jinja

squid:
  service.running:
    - enable: True
    - watch:
      - file: /etc/squid/squid.conf

