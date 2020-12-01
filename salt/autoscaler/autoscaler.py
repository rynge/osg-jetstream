#!/usr/bin/python3

import openstack
import re
import sys
import time

from datetime import datetime, timedelta
from dateutil import parser, tz
from pprint import pprint

# consts
MAX_INSTANCES_TOTAL = 5
MAX_INSTANCES_PER_ITERAION = 1

cloud = openstack.connect(cloud='jetstream_tacc')

servers_running = 0

# clean out shutdown/failed/... machines
for server in cloud.compute.servers():

    #print(server)
    #pprint(server)

    if not re.match('^osg-worker', server.name):
        continue

    created_at = parser.parse(server.created_at, ignoretz=True)
    if not 'updated' in server:
        server.updated = server.created_at
    last_update = parser.parse(server.updated, ignoretz=True)
    now = datetime.utcnow()
    
    print(' ... %s (%s, created %s)' %(server.name, server.status, str(created_at)))

    if server.status == 'SHUTOFF' or server.status == 'ERROR':
        # remove the server
        print('     ... deleting server')
        cloud.delete_server(server)
        continue

    # sometimes the instances get stuck in BUILD state
    if server.status == 'BUILD' and created_at < now - timedelta(hours=2):
        # remove the server
        print('     ... deleting server')
        cloud.delete_server(server)
        continue

    # just stuck
    if last_update < now - timedelta(days=2):
        # remove the server
        print('     ... seems stuck, deleting server')
        cloud.delete_server(server)
        continue

    if server.status == 'ACTIVE' or server.status == 'BUILD':
        servers_running += 1
        continue


print('%d servers running' %(servers_running))

if servers_running >= MAX_INSTANCES_TOTAL:
    print('Max servers running')
    sys.exit(0)

new_instances_count = 1

# bounds
new_instances_count = min(new_instances_count, MAX_INSTANCES_PER_ITERAION)
if MAX_INSTANCES_TOTAL - servers_running < new_instances_count:
    new_instances_count = MAX_INSTANCES_TOTAL - servers_running
if servers_running >= MAX_INSTANCES_TOTAL:
    new_instances_count = 0

print('Starting %d new servers' %(new_instances_count))

for i in range(new_instances_count):
    
    # select image to use
    image_selected = None
    for i in cloud.compute.images():
        #pprint(i)
        if not re.match('^osg-worker-', i.name):
            continue
        if image_selected is None or \
           i.name > image_selected.name:
            image_selected = i
    print('Selected %s for a new instance' %(image_selected.name))

    flavor = cloud.compute.find_flavor('m1.medium')

    # sleep to make sure this is a unique ts
    time.sleep(2)

    network = cloud.network.find_network('internal-net')

    keypair = cloud.compute.find_keypair('rynge-2020')

    dt = datetime.now()
    name = 'osg-worker-%s' %(dt.strftime('%Y%m%d%H%M%S'))

    print('Starting a new instance with name %s' %(name))
    cloud.create_server(name, \
                        image=image_selected, \
                        flavor=flavor, \
                        network=[network], \
                        key_name='rynge-2020', \
                        auto_ip=False)

print('All done')


