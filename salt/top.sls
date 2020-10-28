base:

  'roles:common':
    - match: grain
    - salt
    - dhcp
    - osg

  'roles:control':
    - match: grain
    - squid

