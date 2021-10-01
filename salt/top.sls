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
    - frontier-squid
    - restapi

  'roles:worker':
    - match: grain
    - osgvo-docker-pilot
    - tools

