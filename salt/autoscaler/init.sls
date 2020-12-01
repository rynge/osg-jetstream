
/etc/cron.d/autoscaler:
  file.managed:
    - source: salt://autoscaler/autoscaler.cron
    - user: root
    - group: root
    - mode: 644

