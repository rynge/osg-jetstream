base:

  '*':
    - salt
    - dhcp
    - resolv
    - users
    - osg

  'roles:control':
    - match: grain
    - squid

  'roles:worker':
    - match: grain
    - osgvo-docker-pilot

