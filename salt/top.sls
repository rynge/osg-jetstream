base:

  '*':
    - salt
    - dhcp
    - resolv
    - cloud-init
    - users
    - osg

  'roles:control':
    - match: grain
    - squid
    - restapi

  'roles:worker':
    - match: grain
    - osgvo-docker-pilot

