
/usr/bin/run-osgvo-docker-pilot-container:
  file.managed:
    - source: salt://osgvo-docker-pilot/run-osgvo-docker-pilot-container
    - user: root
    - group: root
    - mode: 755

/etc/systemd/system/osgvo-docker-pilot.service:
  file.managed:
    - source: salt://osgvo-docker-pilot/osgvo-docker-pilot.service
    - user: root
    - group: root
    - mode: 644

osgvo-docker-pilot:
  service.running:
    - enable: True
    - watch:
      - file: /usr/bin/run-osgvo-docker-pilot-container
      - file: /etc/systemd/system/osgvo-docker-pilot.service

