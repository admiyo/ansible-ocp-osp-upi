#!/bin/sh 
ansible-playbook   -e @vars/main.yaml  playbooks/cleanup.yaml
