#!/bin/sh

BASEDIR=$(dirname $0)

cd $1
grunt
cd $BASEDIR