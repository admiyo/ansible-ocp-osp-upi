#!/bin/sh 
ansible-playbook -e @vars/main.yaml playbooks/regen-install-config.yaml
