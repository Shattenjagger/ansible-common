#!/bin/sh

BASEDIR=$(dirname $0)
APP_NAME=$2
DJANGO_DIR=$3
$BASEDIR/parse_current_settings.py $1 $2 $3