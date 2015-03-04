#!/bin/sh

echo "Starting Web app build"

BASEDIR=$(dirname $0)

ansible-playbook -i $BASEDIR/../inventory.ansible $BASEDIR/webapp_deployment.yaml -l $1