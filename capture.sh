#!/bin/bash
PATH=/bin:/usr/bin:/usr/local/bin:/sbin:/usr/sbin:/usr/local/sbin

LOCAL_DATADIR=/home/pi/data
REMOTE_DATADIR=/backup/picam
IMGFILE="${LOCAL_DATADIR}/russet-$(date +'%s').png"

mkdir $LOCAL_DATADIR
raspistill -e png -o $IMGFILE
scp ${LOCAL_DATADIR}/*png rh:${REMOTE_DATADIR} && \
	find ${LOCAL_DATADIR}/ -type f -name \*png -delete
