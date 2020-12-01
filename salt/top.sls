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
    - autoscaler

  'roles:worker':
    - match: grain
    - osgvo-docker-pilot

