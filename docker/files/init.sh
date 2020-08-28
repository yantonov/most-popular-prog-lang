#!/bin/sh

echo 'init'

. /root/init-jupiter.sh

echo "execute $@"
exec $@
