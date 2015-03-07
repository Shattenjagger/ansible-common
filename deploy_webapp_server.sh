#!/bin/sh

BASEDIR=$(dirname $0)
APP_NAME=$2
DJANGO_DIR=$3
$BASEDIR/parse_current_settings.py $1 $2 $3
ansible-playbook -i $BASEDIR/../inventory.ansible $BASEDIR/django_webapp_deployment.yaml -l $1 --extra-vars "{\"django_app\": \"$APP_NAME\"}"