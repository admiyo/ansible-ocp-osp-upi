#!/bin/python3
import base64, json, sys, os;

INFRA_ID = os.environ['INFRA_ID']

for index in range(0, 3):
    with open("master.ign","r") as master_ign_file:
        ignition = json.load(master_ign_file);
    files = ignition['storage'].get('files', []);
    MASTER_HOSTNAME="{}-master-{}".format(INFRA_ID, index);
    files.append({'path': '/etc/hostname', 'mode': 420, 'contents': {'source': 'data:text/plain;charset=utf-8;base64,' + base64.standard_b64encode(b'$MASTER_HOSTNAME').decode().strip(), 'verification': {}}, 'filesystem': 'root'});
    ignition['storage']['files'] = files;
    with open("{}.json".format(MASTER_HOSTNAME), "w") as shim_file:
        json.dump(ignition, shim_file)
