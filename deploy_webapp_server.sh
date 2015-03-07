#!/bin/sh

BASEDIR=$(dirname $0)
APP_NAME=$2
$BASEDIR/parse_current_settings.py $1 $2