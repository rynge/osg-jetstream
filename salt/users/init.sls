
osg:
  group.present:
    - gid: 2000
  user.present:
    - uid: 2000
    - gid: 2000
    - shell: /bin/bash
    - home: /home/osg
    - remove_groups: False
    - groups:
      - osg
      - docker


