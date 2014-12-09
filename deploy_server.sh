#!/bin/bash

BASEDIR=$(dirname $0)
$BASEDIR/parse_current_settings.py $1
ansible-playbook -i $BASEDIR/../inventory.ansible $BASEDIR/deployment.yaml -l $1
ansible-playbook -i $BASEDIR/../inventory.ansible $BASEDIR/django_routines.yaml -l $1